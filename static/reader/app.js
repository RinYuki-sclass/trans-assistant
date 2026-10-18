/**
 * 📖 Cubari Manhwa Reader - Client Application
 */

const state = {
  manga: null,            // { title, slug, chapters: [], source }
  chapterIndex: 0,        // chỉ số chapter hiện tại
  chapterData: null,      // { title, images: [], script: "" }
  currentPage: 1,         // trang hiện tại (1-indexed)
  resumePage: 1,          // trang cần phục hồi khi resume
  readingMode: 'webtoon', // 'webtoon' | 'single' | 'double'
  theme: 'oled',          // 'oled' | 'dark' | 'sepia'
  webtoonWidth: 820,
  stripGap: 0,
  hudVisible: true,
  isSeeking: false,
  downloadTasks: [],
  crawlPreviewInfo: null,
  libraryMangas: [],
  libraryUpdates: {}
};

// DOM Elements
const el = {
  hudTop: document.getElementById('hud-top'),
  hudBottom: document.getElementById('hud-bottom'),
  viewport: document.getElementById('reader-viewport'),
  seriesTitle: document.getElementById('series-title'),
  chapterSelect: document.getElementById('chapter-select'),
  prevChapterBtn: document.getElementById('btn-prev-chapter'),
  nextChapterBtn: document.getElementById('btn-next-chapter'),
  pageCounter: document.getElementById('page-counter'),
  scrubberSlider: document.getElementById('scrubber-slider'),
  modeToggleBtn: document.getElementById('btn-mode-toggle'),
  modeIcon: document.getElementById('mode-icon'),
  modeText: document.getElementById('mode-text'),
  fullscreenBtn: document.getElementById('btn-fullscreen'),
  settingsBtn: document.getElementById('btn-settings'),
  settingsPopover: document.getElementById('settings-popover'),
  settingTheme: document.getElementById('setting-theme'),
  settingWidth: document.getElementById('setting-width'),
  settingGap: document.getElementById('setting-gap'),
  widthVal: document.getElementById('width-val'),
  gapVal: document.getElementById('gap-val'),
  drawerBtn: document.getElementById('btn-open-drawer'),
  drawerCloseBtn: document.getElementById('btn-close-drawer'),
  drawer: document.getElementById('library-drawer'),
  libraryList: document.getElementById('library-list'),
  libraryFilterInput: document.getElementById('library-filter-input'),
  checkUpdatesBtn: document.getElementById('btn-check-updates'),
  crawlModalBtn: document.getElementById('btn-open-crawl'),
  crawlModalCloseBtn: document.getElementById('btn-close-crawl'),
  crawlModal: document.getElementById('crawl-modal'),
  searchTabBtn: document.getElementById('tab-btn-search'),
  urlTabBtn: document.getElementById('tab-btn-url'),
  searchPanel: document.getElementById('tab-panel-search'),
  urlPanel: document.getElementById('tab-panel-url'),
  searchInput: document.getElementById('search-manga-input'),
  searchSubmitBtn: document.getElementById('btn-submit-search'),
  searchResults: document.getElementById('search-results-container'),
  crawlUrlInput: document.getElementById('crawl-url-input'),
  crawlSubmitBtn: document.getElementById('btn-submit-crawl'),
  crawlPreview: document.getElementById('crawl-preview-container'),
  tasksList: document.getElementById('tasks-list'),
  toast: document.getElementById('toast-msg'),
  homeBtn: document.getElementById('btn-home')
};

// ====================================================
// KHỞI TẠO & CÀI ĐẶT
// ====================================================

function initApp() {
  loadSavedSettings();
  bindEvents();
  fetchLibrary();
  pollDownloadTasks();

  // Kiểm tra URL params nếu có
  const urlParams = new URLSearchParams(window.location.search);
  const onlineUrl = urlParams.get('url');
  if (onlineUrl) {
    loadOnlineChapter(onlineUrl);
  } else {
    showWelcomeScreen();
  }
}

function loadSavedSettings() {
  const savedTheme = localStorage.getItem('cubari_theme') || 'oled';
  const savedMode = localStorage.getItem('cubari_mode') || 'webtoon';
  const savedWidth = localStorage.getItem('cubari_width') || '820';
  const savedGap = localStorage.getItem('cubari_gap') || '0';

  setTheme(savedTheme);
  setReadingMode(savedMode);
  setWebtoonWidth(parseInt(savedWidth, 10));
  setStripGap(parseInt(savedGap, 10));

  el.settingTheme.value = state.theme;
  el.settingWidth.value = state.webtoonWidth;
  el.settingGap.value = state.stripGap;
  el.widthVal.textContent = state.webtoonWidth;
  el.gapVal.textContent = state.stripGap;
}

function setTheme(theme) {
  state.theme = theme;
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('cubari_theme', theme);
}

function setReadingMode(mode) {
  state.readingMode = mode;
  localStorage.setItem('cubari_mode', mode);

  if (mode === 'webtoon') {
    el.modeIcon.textContent = '📜';
    el.modeText.textContent = 'Webtoon';
  } else if (mode === 'single') {
    el.modeIcon.textContent = '📖';
    el.modeText.textContent = 'Trang Đơn';
  } else if (mode === 'double') {
    el.modeIcon.textContent = '📖📖';
    el.modeText.textContent = 'Trang Đôi';
  }

  if (state.chapterData && state.chapterData.images.length > 0) {
    renderCurrentChapter();
  }
}

function setWebtoonWidth(width) {
  state.webtoonWidth = width;
  document.documentElement.style.setProperty('--webtoon-max-width', `${width}px`);
  el.widthVal.textContent = width;
  localStorage.setItem('cubari_width', width);
}

function setStripGap(gap) {
  state.stripGap = gap;
  document.documentElement.style.setProperty('--strip-gap', `${gap}px`);
  el.gapVal.textContent = gap;
  localStorage.setItem('cubari_gap', gap);
}

function showToast(msg) {
  el.toast.textContent = msg;
  el.toast.classList.add('show');
  setTimeout(() => el.toast.classList.remove('show'), 2500);
}

// ====================================================
// READING TRACKER & AUTO-RESUME
// ====================================================

const HISTORY_KEY = 'cubari_reading_history';
const READ_CHAPTERS_KEY = 'cubari_read_chapters';

function getAllReadingHistory() {
  try {
    return JSON.parse(localStorage.getItem(HISTORY_KEY) || '{}');
  } catch (e) {
    return {};
  }
}

function getReadingProgress(mangaSlug) {
  if (!mangaSlug) return null;
  const history = getAllReadingHistory();
  return history[mangaSlug] || null;
}

function getGlobalLastRead() {
  const history = getAllReadingHistory();
  const list = Object.values(history);
  if (!list.length) return null;
  list.sort((a, b) => (b.updatedAt || 0) - (a.updatedAt || 0));
  return list[0];
}

function saveReadingProgress(page = 1) {
  if (!state.manga || !state.chapterData) return;
  const mangaSlug = state.manga.slug || (state.chapterData && state.chapterData.title) || 'unknown';
  const curCh = state.manga.chapters ? state.manga.chapters[state.chapterIndex] : null;
  const chapterSlug = curCh ? curCh.slug : (state.chapterData.title || `chapter-${state.chapterIndex + 1}`);
  const chapterTitle = curCh ? curCh.title : state.chapterData.title;

  const history = getAllReadingHistory();
  history[mangaSlug] = {
    mangaSlug: mangaSlug,
    mangaTitle: state.manga.title || mangaSlug,
    chapterIndex: state.chapterIndex,
    chapterSlug: chapterSlug,
    chapterTitle: chapterTitle,
    chapterUrl: curCh ? curCh.url : '',
    sourceType: curCh ? curCh.source_type : (state.chapterData.source || 'local'),
    page: page,
    totalPages: state.chapterData.images ? state.chapterData.images.length : 1,
    updatedAt: Date.now()
  };

  try {
    localStorage.setItem(HISTORY_KEY, JSON.stringify(history));
  } catch (e) {}

  markChapterAsRead(mangaSlug, chapterSlug);
}

function getAllReadChapters() {
  try {
    return JSON.parse(localStorage.getItem(READ_CHAPTERS_KEY) || '{}');
  } catch (e) {
    return {};
  }
}

function markChapterAsRead(mangaSlug, chapterSlug) {
  if (!mangaSlug || !chapterSlug) return;
  const readMap = getAllReadChapters();
  if (!readMap[mangaSlug]) {
    readMap[mangaSlug] = [];
  }
  if (!readMap[mangaSlug].includes(chapterSlug)) {
    readMap[mangaSlug].push(chapterSlug);
    try {
      localStorage.setItem(READ_CHAPTERS_KEY, JSON.stringify(readMap));
    } catch (e) {}
  }
}

function isChapterRead(mangaSlug, chapterSlug) {
  if (!mangaSlug || !chapterSlug) return false;
  const readMap = getAllReadChapters();
  return !!(readMap[mangaSlug] && readMap[mangaSlug].includes(chapterSlug));
}

window.resumeLastReading = function() {
  const lastRead = getGlobalLastRead();
  if (!lastRead) {
    showToast('Chưa có lịch sử đọc gần đây');
    return;
  }

  showToast(`Tiếp tục đọc: ${lastRead.mangaTitle}...`);
  if (lastRead.sourceType === 'online' && lastRead.chapterUrl) {
    loadOnlineChapter(lastRead.chapterUrl, lastRead.page);
  } else {
    loadLocalChapter(lastRead.mangaSlug, lastRead.chapterSlug, lastRead.sourceType || 'local', lastRead.page);
  }
};

// ====================================================
// SMART IMAGE PRELOADING
// ====================================================

function preloadNextImages(startIndex, count = 6) {
  if (!state.chapterData || !state.chapterData.images) return;
  const images = state.chapterData.images;
  const end = Math.min(startIndex + count, images.length);
  for (let i = startIndex; i < end; i++) {
    const src = images[i];
    if (src) {
      const preloadImg = new Image();
      preloadImg.src = src;
    }
  }
}

// ====================================================
// HUD & GIAO DIỆN TƯƠNG TÁC
// ====================================================

function setHudVisibility(visible) {
  state.hudVisible = visible;
  if (visible) {
    el.hudTop.classList.remove('hidden');
    el.hudBottom.classList.remove('hidden');
  } else {
    el.hudTop.classList.add('hidden');
    el.hudBottom.classList.add('hidden');
    el.settingsPopover.classList.remove('active');
  }
}

function toggleHud() {
  setHudVisibility(!state.hudVisible);
}

function toggleFullscreen() {
  if (!document.fullscreenElement) {
    document.documentElement.requestFullscreen().catch(() => {});
  } else {
    if (document.exitFullscreen) {
      document.exitFullscreen();
    }
  }
}

// ====================================================
// RENDER CHAPTER & ĐỌC TRUYỆN
// ====================================================

function showWelcomeScreen() {
  el.seriesTitle.textContent = 'Cubari Manhwa Reader';
  el.chapterSelect.innerHTML = '<option>Sẵn sàng đọc truyện</option>';
  el.pageCounter.textContent = '0 / 0';
  el.scrubberSlider.max = 1;
  el.scrubberSlider.value = 1;

  const lastRead = getGlobalLastRead();
  let resumeHtml = '';
  if (lastRead) {
    resumeHtml = `
      <div class="resume-card" onclick="resumeLastReading()" title="Nhấp để tiếp tục đọc" style="cursor: pointer;">
        <div class="resume-info">
          <div class="resume-info-badge">⚡ Tiếp tục đọc dở</div>
          <div class="resume-info-title">${lastRead.mangaTitle}</div>
          <div class="resume-info-meta">${lastRead.chapterTitle} • Đang đọc trang ${lastRead.page}/${lastRead.totalPages || '?'}</div>
        </div>
        <button class="btn btn-primary" style="padding: 0.55rem 1.1rem; font-size: 0.85rem;">
          Đọc Tiếp ▶
        </button>
      </div>
    `;
  }

  el.viewport.innerHTML = `
    <div style="text-align: center; max-width: 650px; padding: 3.5rem 1.5rem; margin: auto;">
      <div style="font-size: 3.5rem; margin-bottom: 0.8rem;">📖</div>
      <h2 style="font-size: 1.8rem; font-weight: 800; margin-bottom: 0.8rem; letter-spacing: -0.5px;">
        Chào Mừng Đến Với Cubari Manhwa Reader
      </h2>
      <p style="color: var(--text-secondary); line-height: 1.6; font-size: 0.95rem; margin-bottom: 2rem;">
        Trình đọc manhwa tối giản, tải ảnh mượt mà, hỗ trợ cuộn dọc Webtoon vô tận và hoàn toàn không dính quảng cáo rác.
      </p>

      ${resumeHtml}

      <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
        <button class="btn btn-primary" onclick="openCrawlModalWithExample()" style="padding: 0.65rem 1.25rem; font-size: 0.95rem;">
          📥 Thử Tải / Crawl Chapter (haccbl.xyz)
        </button>
        <button class="btn" onclick="openDrawer()" style="padding: 0.65rem 1.25rem; font-size: 0.95rem;">
          📚 Mở Thư Viện Của Tôi
        </button>
      </div>

      <div style="margin-top: 3.5rem; padding: 1.25rem; background: var(--bg-secondary); border: 1px solid var(--border-color); border-radius: 12px; text-align: left;">
        <h4 style="font-size: 0.9rem; margin-bottom: 0.6rem; color: var(--accent-hover);">💡 Phím tắt nhanh:</h4>
        <ul style="font-size: 0.85rem; color: var(--text-secondary); line-height: 1.8; padding-left: 1.2rem;">
          <li><b>Space / Shift+Space:</b> Cuộn xuống / Cuộn lên nửa màn hình</li>
          <li><b>Mũi tên Trái / Phải:</b> Lật trang hoặc Chuyển chương trước / sau</li>
          <li><b>F:</b> Bật / Tắt chế độ toàn màn hình (Fullscreen)</li>
          <li><b>M:</b> Chuyển đổi qua lại giữa chế độ Webtoon và Lật trang</li>
          <li><b>H:</b> Ẩn / Hiện thanh điều khiển (HUD)</li>
        </ul>
      </div>
    </div>
  `;
}

function renderCurrentChapter() {
  if (!state.chapterData || !state.chapterData.images.length) return;

  const total = state.chapterData.images.length;
  el.scrubberSlider.min = 1;
  el.scrubberSlider.max = total;
  el.scrubberSlider.value = state.currentPage;
  updatePageCounter(state.currentPage, total);

  if (state.readingMode === 'webtoon') {
    renderWebtoonMode();
  } else if (state.readingMode === 'single') {
    renderSinglePageMode();
  } else if (state.readingMode === 'double') {
    renderDoublePageMode();
  }
}

// 1. Chế độ Webtoon (Cuộn dọc)
function renderWebtoonMode() {
  el.viewport.innerHTML = '';
  const strip = document.createElement('div');
  strip.className = 'webtoon-strip';

  state.chapterData.images.forEach((imgSrc, index) => {
    const img = document.createElement('img');
    img.src = imgSrc;
    img.dataset.page = index + 1;
    img.loading = index < 3 ? 'eager' : 'lazy';
    img.alt = `Trang ${index + 1}`;

    // Xử lý ảnh lỗi kết nối / timeout
    img.onerror = () => {
      const errorCard = document.createElement('div');
      errorCard.className = 'img-error-card';
      errorCard.dataset.page = index + 1;
      errorCard.innerHTML = `
        <span>⚠️ Không thể tải trang ${index + 1} (Lỗi mạng hoặc CDN nguồn)</span>
        <button class="btn-retry">🔄 Nhấp để tải lại</button>
      `;
      const btnRetry = errorCard.querySelector('.btn-retry');
      btnRetry.onclick = (e) => {
        e.stopPropagation();
        const sep = imgSrc.includes('?') ? '&' : '?';
        img.src = `${imgSrc}${sep}_retry=${Date.now()}`;
        errorCard.replaceWith(img);
      };
      img.replaceWith(errorCard);
    };

    strip.appendChild(img);
  });

  // Card chuyển chapter ở cuối strip
  const navCard = document.createElement('div');
  navCard.className = 'chapter-nav-card';
  navCard.innerHTML = `
    <h3>🎉 Đã đọc hết chương!</h3>
    <p>${state.chapterData.title || ''}</p>
    <div class="chapter-nav-actions">
      <button class="btn" id="btn-end-prev" ${state.chapterIndex <= 0 ? 'disabled' : ''}>◀ Chương Trước</button>
      <button class="btn btn-primary" id="btn-end-next" ${state.chapterIndex >= (state.manga?.chapters?.length || 1) - 1 ? 'disabled' : ''}>Chương Tiếp Theo ▶</button>
      <button class="btn" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">⬆ Đầu Trang</button>
    </div>
  `;
  strip.appendChild(navCard);
  el.viewport.appendChild(strip);

  // Gán sự kiện cho nút cuối trang
  const endPrev = navCard.querySelector('#btn-end-prev');
  const endNext = navCard.querySelector('#btn-end-next');
  if (endPrev) endPrev.onclick = goToPrevChapter;
  if (endNext) endNext.onclick = goToNextChapter;

  setupWebtoonScrollObserver();

  // Bắt đầu preloading 6 ảnh đầu tiên
  preloadNextImages(0, 6);

  // Khôi phục trang đọc dở nếu có resumePage
  if (state.resumePage && state.resumePage > 1) {
    const targetPage = state.resumePage;
    state.resumePage = 1;
    setTimeout(() => {
      const targetImg = document.querySelector(`.webtoon-strip img[data-page="${targetPage}"]`);
      if (targetImg) {
        targetImg.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 250);
  } else {
    window.scrollTo({ top: 0, behavior: 'instant' });
  }
}

// Observer theo dõi trang đang hiển thị khi cuộn
let scrollObserver = null;
function setupWebtoonScrollObserver() {
  if (scrollObserver) scrollObserver.disconnect();

  const options = {
    root: null,
    rootMargin: '-20% 0px -60% 0px',
    threshold: 0
  };

  scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !state.isSeeking) {
        const page = parseInt(entry.target.dataset.page, 10);
        if (page) {
          state.currentPage = page;
          el.scrubberSlider.value = page;
          updatePageCounter(page, state.chapterData.images.length);
          saveReadingProgress(page);
          preloadNextImages(page, 6);
        }
      }
    });
  }, options);

  document.querySelectorAll('.webtoon-strip img').forEach(img => {
    scrollObserver.observe(img);
  });
}

// 2. Chế độ Single Page
function renderSinglePageMode() {
  el.viewport.innerHTML = '';
  const container = document.createElement('div');
  container.className = 'page-turn-mode';

  const img = document.createElement('img');
  img.src = state.chapterData.images[state.currentPage - 1];
  img.alt = `Trang ${state.currentPage}`;

  // Click zones
  const leftZone = document.createElement('div');
  leftZone.className = 'click-zone click-zone-left';
  leftZone.title = 'Trang trước';
  leftZone.onclick = prevPage;

  const rightZone = document.createElement('div');
  rightZone.className = 'click-zone click-zone-right';
  rightZone.title = 'Trang sau';
  rightZone.onclick = nextPage;

  container.appendChild(leftZone);
  container.appendChild(img);
  container.appendChild(rightZone);

  container.onclick = (e) => {
    // Nếu click vào giữa -> bật tắt HUD
    if (e.target === container || e.target === img) {
      toggleHud();
    }
  };

  el.viewport.appendChild(container);
}

// 3. Chế độ Double Page
function renderDoublePageMode() {
  el.viewport.innerHTML = '';
  const container = document.createElement('div');
  container.className = 'page-turn-mode';

  const doubleWrap = document.createElement('div');
  doubleWrap.className = 'double-page-container';

  const curIdx = state.currentPage - 1;
  const img1 = document.createElement('img');
  img1.src = state.chapterData.images[curIdx];

  doubleWrap.appendChild(img1);

  if (curIdx + 1 < state.chapterData.images.length) {
    const img2 = document.createElement('img');
    img2.src = state.chapterData.images[curIdx + 1];
    doubleWrap.appendChild(img2);
  }

  const leftZone = document.createElement('div');
  leftZone.className = 'click-zone click-zone-left';
  leftZone.onclick = () => {
    state.currentPage = Math.max(1, state.currentPage - 2);
    renderDoublePageMode();
    updatePageCounter(state.currentPage, state.chapterData.images.length);
    el.scrubberSlider.value = state.currentPage;
  };

  const rightZone = document.createElement('div');
  rightZone.className = 'click-zone click-zone-right';
  rightZone.onclick = () => {
    if (state.currentPage + 2 <= state.chapterData.images.length) {
      state.currentPage += 2;
    } else {
      goToNextChapter();
      return;
    }
    renderDoublePageMode();
    updatePageCounter(state.currentPage, state.chapterData.images.length);
    el.scrubberSlider.value = state.currentPage;
  };

  container.appendChild(leftZone);
  container.appendChild(doubleWrap);
  container.appendChild(rightZone);

  el.viewport.appendChild(container);
}

function prevPage() {
  if (state.currentPage > 1) {
    state.currentPage--;
    renderCurrentChapter();
  } else {
    goToPrevChapter();
  }
}

function nextPage() {
  if (state.currentPage < state.chapterData.images.length) {
    state.currentPage++;
    renderCurrentChapter();
  } else {
    goToNextChapter();
  }
}

function updatePageCounter(cur, total) {
  el.pageCounter.textContent = `${cur} / ${total}`;
}

// ====================================================
// NẠP DỮ LIỆU CHAPTER (LOCAL & ONLINE)
// ====================================================

async function loadLocalChapter(mangaSlug, chapterSlug, source = 'local', targetPage = 1) {
  try {
    showToast(`Đang nạp chapter: ${chapterSlug}...`);
    const res = await fetch(`/api/chapter-data?source=${source}&manga_slug=${encodeURIComponent(mangaSlug)}&chapter_slug=${encodeURIComponent(chapterSlug)}`);
    const data = await res.json();
    if (data.status !== 'success') {
      showToast(data.message || 'Không thể tải chapter');
      return;
    }

    state.chapterData = data;
    state.currentPage = targetPage;
    state.resumePage = targetPage;
    el.seriesTitle.textContent = data.title || mangaSlug;
    renderCurrentChapter();
    updateChapterNavigationUI();
    saveReadingProgress(targetPage);
    showToast(`Đã nạp ${data.total} trang ảnh!`);
  } catch (e) {
    showToast(`Lỗi: ${e.message}`);
  }
}

async function loadOnlineChapter(chapterUrl, targetPage = 1) {
  try {
    showToast('Đang giải mã và kết nối chapter online...');
    const res = await fetch(`/api/chapter-data?source=online&url=${encodeURIComponent(chapterUrl)}`);
    const data = await res.json();
    if (data.status !== 'success') {
      showToast(data.message || 'Không thể mở chapter online');
      return;
    }

    state.chapterData = data;
    state.currentPage = targetPage;
    state.resumePage = targetPage;
    el.seriesTitle.textContent = data.title || 'Online Chapter';
    renderCurrentChapter();
    updateChapterNavigationUI();
    saveReadingProgress(targetPage);
    showToast(`Sẵn sàng đọc: ${data.total} trang ảnh không ads!`);
  } catch (e) {
    showToast(`Lỗi: ${e.message}`);
  }
}

function updateChapterNavigationUI() {
  if (!state.manga || !state.manga.chapters) {
    el.prevChapterBtn.disabled = true;
    el.nextChapterBtn.disabled = true;
    return;
  }

  el.prevChapterBtn.disabled = state.chapterIndex <= 0;
  el.nextChapterBtn.disabled = state.chapterIndex >= state.manga.chapters.length - 1;

  // Cập nhật dropdown có tiền tố checkmark cho chapter đã đọc
  el.chapterSelect.innerHTML = '';
  state.manga.chapters.forEach((ch, idx) => {
    const opt = document.createElement('option');
    opt.value = idx;
    const isRead = isChapterRead(state.manga.slug, ch.slug);
    const readPrefix = isRead ? '✓ ' : '';
    opt.textContent = `${readPrefix}${ch.title || `Chapter ${idx + 1}`}`;
    if (idx === state.chapterIndex) opt.selected = true;
    el.chapterSelect.appendChild(opt);
  });
}

function goToPrevChapter() {
  if (state.manga && state.chapterIndex > 0) {
    state.chapterIndex--;
    const ch = state.manga.chapters[state.chapterIndex];
    if (ch.source_type === 'local' || ch.source_type === 'trans_tool') {
      loadLocalChapter(ch.manga_slug, ch.slug, ch.source_type);
    } else if (ch.url) {
      loadOnlineChapter(ch.url);
    }
  } else {
    showToast('Đây là chương đầu tiên');
  }
}

function goToNextChapter() {
  if (state.manga && state.chapterIndex < state.manga.chapters.length - 1) {
    state.chapterIndex++;
    const ch = state.manga.chapters[state.chapterIndex];
    if (ch.source_type === 'local' || ch.source_type === 'trans_tool') {
      loadLocalChapter(ch.manga_slug, ch.slug, ch.source_type);
    } else if (ch.url) {
      loadOnlineChapter(ch.url);
    }
  } else {
    showToast('Đây là chương mới nhất');
  }
}

// ====================================================
// THƯ VIỆN & CRAWLER MODAL
// ====================================================

async function fetchLibrary() {
  try {
    const res = await fetch('/api/library');
    const data = await res.json();
    if (data.status === 'success') {
      renderLibraryDrawer(data.mangas || []);
    }
  } catch (e) {
    console.error('Lỗi nạp thư viện:', e);
  }
}

async function fetchLibrary() {
  try {
    const res = await fetch('/api/library');
    const data = await res.json();
    if (data.status === 'success') {
      state.libraryMangas = data.mangas || [];
      renderLibraryCards(state.libraryMangas);
    }
  } catch (e) {
    console.error('Lỗi nạp thư viện:', e);
  }
}

function renderLibraryCards(mangas) {
  if (!mangas.length) {
    el.libraryList.innerHTML = `
      <div style="text-align: center; color: var(--text-muted); padding: 2rem 1rem;">
        <p style="font-size: 2rem; margin-bottom: 0.5rem;">📂</p>
        <p style="font-size: 0.85rem;">Chưa có bộ truyện nào ở local.</p>
        <button class="btn btn-primary" onclick="openCrawlModalWithExample()" style="margin-top: 1rem; width: 100%;">
          Tải truyện ngay
        </button>
      </div>
    `;
    return;
  }

  el.libraryList.innerHTML = '';
  mangas.forEach(manga => {
    const card = document.createElement('div');
    card.className = 'library-card';
    const progress = getReadingProgress(manga.slug);
    const progressInfo = progress ? `<div style="font-size: 0.75rem; color: var(--accent-hover); margin-top: 0.25rem;">📖 Đang đọc: ${progress.chapterTitle} (Trang ${progress.page})</div>` : '';

    const updateInfo = state.libraryUpdates[manga.slug];
    const updateBadge = updateInfo ? `
      <span class="update-badge" title="Có chương mới trên web nguồn" onclick="event.stopPropagation(); openUpdateForManga('${manga.slug}')">
        ⚡ Có ${updateInfo.new_chapters_count} chương mới
      </span>
    ` : '';

    const deleteBtn = manga.source !== 'trans_tool' ? `
      <button class="btn-delete-manga" title="Xóa bộ truyện này khỏi máy" onclick="event.stopPropagation(); deleteMangaFromLibrary('${manga.slug}', '${encodeURIComponent(manga.title)}')">
        🗑️
      </button>
    ` : '';

    card.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: flex-start; gap: 0.5rem;">
        <div class="library-card-title">${manga.title}</div>
        ${deleteBtn}
      </div>
      <div class="library-card-subtitle">
        ${manga.total_chapters} chương • Nguồn: ${manga.source === 'trans_tool' ? 'Trans-Tool' : 'Local'}
      </div>
      ${progressInfo}
      ${updateBadge ? `<div style="margin-top: 0.4rem;">${updateBadge}</div>` : ''}
    `;

    card.onclick = () => {
      state.manga = manga;
      let targetIdx = 0;
      let targetPage = 1;
      if (progress && typeof progress.chapterIndex === 'number' && manga.chapters[progress.chapterIndex]) {
        targetIdx = progress.chapterIndex;
        targetPage = progress.page || 1;
      }
      state.chapterIndex = targetIdx;
      const ch = manga.chapters[targetIdx];
      if (ch) {
        loadLocalChapter(ch.manga_slug, ch.slug, ch.source_type, targetPage);
        closeDrawer();
      }
    };
    el.libraryList.appendChild(card);
  });
}

function filterLibrary(query) {
  const q = (query || '').trim().toLowerCase();
  if (!q) {
    renderLibraryCards(state.libraryMangas);
    return;
  }
  const filtered = state.libraryMangas.filter(m => m.title.toLowerCase().includes(q));
  renderLibraryCards(filtered);
}

window.checkLibraryUpdates = async function() {
  if (el.checkUpdatesBtn) {
    el.checkUpdatesBtn.disabled = true;
    el.checkUpdatesBtn.textContent = '⏳ Đang quét...';
  }
  showToast('Đang quét các chương mới từ web nguồn...');
  try {
    const res = await fetch('/api/library/check-updates', { method: 'POST' });
    const data = await res.json();
    if (data.status === 'success') {
      const updates = data.updates || [];
      state.libraryUpdates = {};
      updates.forEach(up => {
        state.libraryUpdates[up.manga_slug] = up;
      });
      renderLibraryCards(state.libraryMangas);
      if (updates.length > 0) {
        showToast(`🎉 Phát hiện ${updates.length} bộ truyện có chương mới!`);
      } else {
        showToast('Tất cả các bộ truyện đã được cập nhật mới nhất!');
      }
    } else {
      showToast(data.message || 'Lỗi khi kiểm tra chương mới');
    }
  } catch (e) {
    showToast(`Lỗi: ${e.message}`);
  } finally {
    if (el.checkUpdatesBtn) {
      el.checkUpdatesBtn.disabled = false;
      el.checkUpdatesBtn.textContent = '🔄 Kiểm Tra Chương Mới';
    }
  }
};

window.openUpdateForManga = function(slug) {
  const up = state.libraryUpdates[slug];
  if (!up || !up.source_url) return;
  closeDrawer();
  openCrawlModalWithExample();
  switchCrawlTab('url');
  el.crawlUrlInput.value = up.source_url;
  submitCrawl();
};

window.deleteMangaFromLibrary = async function(slug, encodedTitle) {
  const title = decodeURIComponent(encodedTitle);
  if (!confirm(`Bạn có chắc chắn muốn xóa bộ truyện "${title}" khỏi máy? Toàn bộ các chương đã tải sẽ bị xóa.`)) {
    return;
  }
  try {
    const res = await fetch('/api/library/delete', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ slug })
    });
    const data = await res.json();
    if (data.status === 'success') {
      showToast(`Đã xóa bộ truyện: ${title}`);
      fetchLibrary();
    } else {
      showToast(data.message || 'Không thể xóa');
    }
  } catch (e) {
    showToast(`Lỗi: ${e.message}`);
  }
};

function openDrawer() {
  fetchLibrary();
  el.drawer.classList.add('active');
}

function closeDrawer() {
  el.drawer.classList.remove('active');
}

function openCrawlModalWithExample() {
  el.crawlModal.classList.add('active');
  if (!el.crawlUrlInput.value) {
    el.crawlUrlInput.value = 'https://haccbl.xyz/manga/dia-nguc-cua-kien-yeon-deop/';
  }
}

function switchCrawlTab(tab) {
  if (tab === 'search') {
    el.searchTabBtn.classList.add('active');
    el.urlTabBtn.classList.remove('active');
    el.searchPanel.classList.add('active');
    el.urlPanel.classList.remove('active');
  } else {
    el.urlTabBtn.classList.add('active');
    el.searchTabBtn.classList.remove('active');
    el.urlPanel.classList.add('active');
    el.searchPanel.classList.remove('active');
  }
}

async function submitSearchManga() {
  const query = el.searchInput.value.trim();
  if (!query) {
    showToast('Vui lòng nhập từ khóa tìm kiếm');
    return;
  }

  el.searchSubmitBtn.disabled = true;
  el.searchSubmitBtn.textContent = '⏳ Đang tìm...';
  el.searchResults.style.display = 'block';
  el.searchResults.innerHTML = `
    <div style="text-align: center; padding: 2rem; color: var(--text-secondary);">
      <p style="font-size: 1.5rem; margin-bottom: 0.5rem;">🔍</p>
      <p>Đang tìm kiếm trên các nguồn truyện...</p>
    </div>
  `;

  try {
    const res = await fetch(`/api/crawl/search?q=${encodeURIComponent(query)}`);
    const data = await res.json();
    if (data.status !== 'success') {
      el.searchResults.innerHTML = `<div style="color: var(--danger); padding: 1rem;">❌ ${data.message || 'Lỗi tìm kiếm'}</div>`;
      return;
    }

    const results = data.results || [];
    if (!results.length) {
      el.searchResults.innerHTML = `
        <div style="text-align: center; color: var(--text-muted); padding: 2rem 1rem;">
          <p style="font-size: 1.5rem; margin-bottom: 0.4rem;">😕</p>
          <p>Không tìm thấy kết quả phù hợp cho "${query}".</p>
        </div>
      `;
      return;
    }

    let html = '<div class="search-results-grid">';
    results.forEach(item => {
      const coverSrc = item.cover ? `/api/proxy-image?url=${encodeURIComponent(item.cover)}` : '';
      html += `
        <div class="search-item-card" onclick="selectMangaFromSearch('${encodeURIComponent(item.url)}')">
          <img src="${coverSrc}" class="search-item-cover" alt="Cover" onerror="this.style.display='none'">
          <div class="search-item-meta">
            <div class="search-item-title" title="${item.title}">${item.title}</div>
            <div class="search-item-source">Nguồn: ${item.source} • Nhấp để xem chương ➔</div>
          </div>
        </div>
      `;
    });
    html += '</div>';
    el.searchResults.innerHTML = html;
  } catch (e) {
    el.searchResults.innerHTML = `<div style="color: var(--danger); padding: 1rem;">❌ Lỗi: ${e.message}</div>`;
  } finally {
    el.searchSubmitBtn.disabled = false;
    el.searchSubmitBtn.textContent = '🔍 Tìm Kiếm';
  }
}

window.selectMangaFromSearch = function(encodedUrl) {
  const url = decodeURIComponent(encodedUrl);
  switchCrawlTab('url');
  el.crawlUrlInput.value = url;
  submitCrawl();
};

// Xử lý Crawl URL
async function submitCrawl() {
  const url = el.crawlUrlInput.value.trim();
  if (!url) {
    showToast('Vui lòng nhập đường dẫn URL');
    return;
  }

  el.crawlSubmitBtn.disabled = true;
  el.crawlSubmitBtn.textContent = '⏳ Đang quét...';
  el.crawlPreview.style.display = 'block';
  el.crawlPreview.innerHTML = `
    <div style="text-align: center; padding: 2rem; color: var(--text-secondary);">
      <p style="font-size: 1.5rem; margin-bottom: 0.5rem;">🔍</p>
      <p>Đang bóc tách thông tin truyện & vượt rào bảo vệ...</p>
    </div>
  `;

  try {
    const res = await fetch('/api/crawl/info', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ url })
    });
    const result = await res.json();

    if (result.status !== 'success') {
      el.crawlPreview.innerHTML = `
        <div style="color: var(--danger); padding: 1rem; background: rgba(239,68,68,0.1); border-radius: 8px;">
          ❌ ${result.message || 'Không thể phân tích URL này'}
        </div>
      `;
      return;
    }

    const info = result.data;
    renderCrawlPreview(info);
  } catch (e) {
    el.crawlPreview.innerHTML = `
      <div style="color: var(--danger); padding: 1rem;">❌ Lỗi: ${e.message}</div>
    `;
  } finally {
    el.crawlSubmitBtn.disabled = false;
    el.crawlSubmitBtn.textContent = '🔍 Phân Tích';
  }
}

function renderCrawlPreview(info) {
  state.crawlPreviewInfo = info;
  let chaptersHtml = '';
  info.chapters.forEach((ch, idx) => {
    const isRead = isChapterRead(info.slug, ch.slug);
    const readBadge = isRead ? `<span class="chapter-badge-read">Đã đọc</span>` : '';
    const readClass = isRead ? ' is-read' : '';

    chaptersHtml += `
      <div class="chapter-item${readClass}" id="ch-item-${idx}">
        <div style="display: flex; align-items: center; gap: 0.5rem; flex: 1; overflow: hidden;">
          <input type="checkbox" class="chapter-item-checkbox" data-idx="${idx}" onchange="updateSelectedCount()">
          <span class="chapter-item-title" title="${ch.title}">${ch.title}</span>
          ${readBadge}
        </div>
        <div style="display: flex; gap: 0.35rem;">
          <button class="btn btn-icon" style="font-size: 0.75rem; padding: 0.25rem 0.5rem;" 
                  onclick="readOnlineFromPreview(${idx})">
            ⚡ Đọc Ngay
          </button>
          <button class="btn btn-primary" style="font-size: 0.75rem; padding: 0.25rem 0.5rem;"
                  onclick="startDownloadChapter('${encodeURIComponent(info.title)}', '${info.slug}', '${encodeURIComponent(ch.title)}', '${ch.slug}', '${ch.url}')">
            📥 Tải Về
          </button>
        </div>
      </div>
    `;
  });

  el.crawlPreview.innerHTML = `
    <div class="manga-preview">
      <img src="${info.cover ? `/api/proxy-image?url=${encodeURIComponent(info.cover)}` : ''}" class="manga-cover" alt="Cover">
      <div class="manga-meta">
        <div>
          <h4>${info.title}</h4>
          <p>Tổng cộng: <b>${info.total_chapters}</b> chương</p>
        </div>
        <div style="display: flex; gap: 0.5rem; margin-top: 0.5rem;">
          <button class="btn btn-primary" style="font-size: 0.8rem;"
                  onclick="downloadAllChapters()">
            📥 Tải Toàn Bộ Chương
          </button>
        </div>
      </div>
    </div>

    <!-- Khung chọn dải chương & tải hàng loạt -->
    <div class="range-select-box">
      <div class="range-inputs">
        <span>Từ:</span>
        <input type="number" id="range-from" class="range-input-num" min="1" max="${info.chapters.length}" value="1">
        <span>Đến:</span>
        <input type="number" id="range-to" class="range-input-num" min="1" max="${info.chapters.length}" value="${Math.min(10, info.chapters.length)}">
        <button class="btn" style="font-size: 0.75rem; padding: 0.25rem 0.55rem;" onclick="applyRangeSelect()">Chọn dải</button>
      </div>
      <div class="batch-btn-bar">
        <button class="btn" style="font-size: 0.75rem; padding: 0.25rem 0.5rem;" onclick="selectLatestChapters(5)">5 mới nhất</button>
        <button class="btn" style="font-size: 0.75rem; padding: 0.25rem 0.5rem;" onclick="selectLatestChapters(10)">10 mới nhất</button>
        <button class="btn" style="font-size: 0.75rem; padding: 0.25rem 0.5rem;" onclick="selectAllChapters(true)">Tất cả</button>
        <button class="btn" style="font-size: 0.75rem; padding: 0.25rem 0.5rem;" onclick="selectAllChapters(false)">Bỏ chọn</button>
        <button class="btn btn-primary" id="btn-batch-download" style="font-size: 0.75rem; padding: 0.25rem 0.65rem;" onclick="downloadSelectedChapters()">
          📥 Tải đã chọn (<span id="selected-count">0</span>)
        </button>
      </div>
    </div>

    <div class="chapter-list-grid">
      ${chaptersHtml}
    </div>
  `;
}

// Bắt đầu đọc online trực tiếp từ preview
window.readOnlineFromPreview = function(chapterIdx) {
  if (!state.crawlPreviewInfo) return;
  const info = state.crawlPreviewInfo;
  state.manga = info;
  state.chapterIndex = chapterIdx;
  const targetCh = info.chapters[chapterIdx];
  el.crawlModal.classList.remove('active');
  loadOnlineChapter(targetCh.url);
};

// Chọn dải chương
window.applyRangeSelect = function() {
  if (!state.crawlPreviewInfo) return;
  const fromVal = parseInt(document.getElementById('range-from').value, 10);
  const toVal = parseInt(document.getElementById('range-to').value, 10);
  const start = Math.max(1, Math.min(fromVal, toVal));
  const end = Math.min(state.crawlPreviewInfo.chapters.length, Math.max(fromVal, toVal));

  document.querySelectorAll('.chapter-item-checkbox').forEach((cb, idx) => {
    const chNum = idx + 1;
    cb.checked = (chNum >= start && chNum <= end);
  });
  window.updateSelectedCount();
  showToast(`Đã chọn từ chương ${start} đến ${end}`);
};

// Chọn N chương mới nhất
window.selectLatestChapters = function(count) {
  if (!state.crawlPreviewInfo) return;
  const total = state.crawlPreviewInfo.chapters.length;
  const start = Math.max(0, total - count);

  document.querySelectorAll('.chapter-item-checkbox').forEach((cb, idx) => {
    cb.checked = (idx >= start);
  });
  window.updateSelectedCount();
  showToast(`Đã chọn ${Math.min(count, total)} chương mới nhất`);
};

// Chọn tất cả hoặc bỏ chọn
window.selectAllChapters = function(select) {
  document.querySelectorAll('.chapter-item-checkbox').forEach(cb => {
    cb.checked = !!select;
  });
  window.updateSelectedCount();
  showToast(select ? 'Đã chọn toàn bộ chương' : 'Đã bỏ chọn toàn bộ');
};

// Cập nhật số lượng đã chọn
window.updateSelectedCount = function() {
  const selected = document.querySelectorAll('.chapter-item-checkbox:checked').length;
  const countEl = document.getElementById('selected-count');
  if (countEl) countEl.textContent = selected;
};

// Tải các chapter đã chọn
window.downloadSelectedChapters = async function() {
  if (!state.crawlPreviewInfo) return;
  const selectedCbs = Array.from(document.querySelectorAll('.chapter-item-checkbox:checked'));
  if (!selectedCbs.length) {
    showToast('Chưa chọn chương nào để tải!');
    return;
  }

  showToast(`Đang đưa ${selectedCbs.length} chương đã chọn vào hàng đợi tải...`);
  const info = state.crawlPreviewInfo;
  for (const cb of selectedCbs) {
    const idx = parseInt(cb.dataset.idx, 10);
    const ch = info.chapters[idx];
    if (ch) {
      await window.startDownloadChapter(
        encodeURIComponent(info.title),
        info.slug,
        encodeURIComponent(ch.title),
        ch.slug,
        ch.url
      );
    }
  }
};

// Gửi lệnh tải 1 chapter
window.startDownloadChapter = async function(mangaTitle, mangaSlug, chapterTitle, chapterSlug, chapterUrl) {
  try {
    showToast(`Đã đưa chapter vào hàng đợi tải...`);
    const mangaUrl = state.crawlPreviewInfo ? state.crawlPreviewInfo.url : '';
    const res = await fetch('/api/crawl/download', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        manga_title: decodeURIComponent(mangaTitle),
        manga_slug: mangaSlug,
        chapter_title: decodeURIComponent(chapterTitle),
        chapter_slug: chapterSlug,
        chapter_url: chapterUrl,
        manga_url: mangaUrl
      })
    });
    const result = await res.json();
    if (result.status === 'success') {
      showToast('Bắt đầu tải về máy!');
      pollDownloadTasks();
    }
  } catch (e) {
    showToast(`Lỗi: ${e.message}`);
  }
};

// Tải tất cả các chapter
window.downloadAllChapters = async function() {
  if (!state.crawlPreviewInfo) return;
  const info = state.crawlPreviewInfo;
  showToast(`Đang thêm ${info.chapters.length} chương vào hàng đợi tải...`);
  for (const ch of info.chapters) {
    await window.startDownloadChapter(
      encodeURIComponent(info.title),
      info.slug,
      encodeURIComponent(ch.title),
      ch.slug,
      ch.url
    );
  }
};

// Polling tiến trình tải về
let pollTimer = null;
async function pollDownloadTasks() {
  clearTimeout(pollTimer);
  try {
    const res = await fetch('/api/crawl/tasks');
    const data = await res.json();
    if (data.status === 'success') {
      const tasks = data.tasks || [];
      renderDownloadTasks(tasks);

      // Nếu có task đang tải, tiếp tục poll mỗi 1.5s
      const isAnyActive = tasks.some(t => t.status === 'downloading' || t.status === 'pending');
      if (isAnyActive) {
        pollTimer = setTimeout(pollDownloadTasks, 1500);
      }
    }
  } catch (e) {
    // silently ignore network errors during poll
  }
}

function renderDownloadTasks(tasks) {
  if (!tasks.length) {
    el.tasksList.innerHTML = `<p style="color: var(--text-muted); font-size: 0.8rem;">Chưa có tiến trình tải nào.</p>`;
    return;
  }

  el.tasksList.innerHTML = '';
  tasks.slice().reverse().forEach(task => {
    const card = document.createElement('div');
    card.className = 'task-card';

    let statusBadge = `<span style="color: var(--accent-hover);">⏳ ${task.percent || 0}%</span>`;
    if (task.status === 'completed') {
      statusBadge = `<span style="color: var(--success);">✅ Hoàn tất</span>`;
    } else if (task.status === 'failed') {
      statusBadge = `<span style="color: var(--danger);">❌ Thất bại</span>`;
    }

    card.innerHTML = `
      <div class="task-info">
        <span><b>${task.chapter_title}</b> (${task.manga_title})</span>
        ${statusBadge}
      </div>
      <div class="progress-bar-bg">
        <div class="progress-bar-fill" style="width: ${task.percent || 0}%;"></div>
      </div>
      <div style="font-size: 0.75rem; color: var(--text-muted); margin-top: 0.35rem;">
        ${task.message || ''}
      </div>
    `;
    el.tasksList.appendChild(card);
  });
}

// ====================================================
// SỰ KIỆN & PHÍM TẮT
// ====================================================

function bindEvents() {
  // Navigation & Buttons
  el.prevChapterBtn.onclick = goToPrevChapter;
  el.nextChapterBtn.onclick = goToNextChapter;
  el.fullscreenBtn.onclick = toggleFullscreen;
  el.homeBtn.onclick = showWelcomeScreen;

  el.chapterSelect.onchange = (e) => {
    const idx = parseInt(e.target.value, 10);
    if (!isNaN(idx) && state.manga && state.manga.chapters[idx]) {
      state.chapterIndex = idx;
      const ch = state.manga.chapters[idx];
      if (ch.source_type === 'local' || ch.source_type === 'trans_tool') {
        loadLocalChapter(ch.manga_slug, ch.slug, ch.source_type);
      } else if (ch.url) {
        loadOnlineChapter(ch.url);
      }
    }
  };

  // Toggle Mode
  el.modeToggleBtn.onclick = () => {
    const modes = ['webtoon', 'single', 'double'];
    const nextIdx = (modes.indexOf(state.readingMode) + 1) % modes.length;
    setReadingMode(modes[nextIdx]);
    showToast(`Chế độ: ${el.modeText.textContent}`);
  };

  // Scrubber Slider
  el.scrubberSlider.oninput = (e) => {
    state.isSeeking = true;
    const page = parseInt(e.target.value, 10);
    state.currentPage = page;
    updatePageCounter(page, state.chapterData?.images?.length || 1);

    if (state.readingMode === 'webtoon') {
      const targetImg = document.querySelector(`.webtoon-strip img[data-page="${page}"]`);
      if (targetImg) {
        targetImg.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    } else {
      renderCurrentChapter();
    }
  };

  el.scrubberSlider.onchange = () => {
    setTimeout(() => { state.isSeeking = false; }, 300);
  };

  // Settings
  el.settingsBtn.onclick = () => {
    el.settingsPopover.classList.toggle('active');
  };

  el.settingTheme.onchange = (e) => setTheme(e.target.value);
  el.settingWidth.oninput = (e) => setWebtoonWidth(parseInt(e.target.value, 10));
  el.settingGap.oninput = (e) => setStripGap(parseInt(e.target.value, 10));

  // Drawer & Filter
  el.drawerBtn.onclick = openDrawer;
  el.drawerCloseBtn.onclick = closeDrawer;
  if (el.libraryFilterInput) {
    el.libraryFilterInput.oninput = (e) => filterLibrary(e.target.value);
  }
  if (el.checkUpdatesBtn) {
    el.checkUpdatesBtn.onclick = window.checkLibraryUpdates;
  }

  // Crawl Modal & Search Tabs
  el.crawlModalBtn.onclick = openCrawlModalWithExample;
  el.crawlModalCloseBtn.onclick = () => el.crawlModal.classList.remove('active');
  el.crawlSubmitBtn.onclick = submitCrawl;
  el.crawlUrlInput.onkeydown = (e) => {
    if (e.key === 'Enter') submitCrawl();
  };

  if (el.searchTabBtn) {
    el.searchTabBtn.onclick = () => switchCrawlTab('search');
  }
  if (el.urlTabBtn) {
    el.urlTabBtn.onclick = () => switchCrawlTab('url');
  }
  if (el.searchSubmitBtn) {
    el.searchSubmitBtn.onclick = submitSearchManga;
  }
  if (el.searchInput) {
    el.searchInput.onkeydown = (e) => {
      if (e.key === 'Enter') submitSearchManga();
    };
  }

  // Keyboard Shortcuts
  window.addEventListener('keydown', (e) => {
    // Không nhận hotkey khi đang gõ text trong modal
    if (['INPUT', 'SELECT', 'TEXTAREA'].includes(document.activeElement.tagName)) return;

    switch (e.key.toLowerCase()) {
      case 'arrowleft':
        prevPage();
        break;
      case 'arrowright':
        nextPage();
        break;
      case ' ':
        e.preventDefault();
        window.scrollBy({ top: e.shiftKey ? -window.innerHeight * 0.75 : window.innerHeight * 0.75, behavior: 'smooth' });
        break;
      case 'f':
        toggleFullscreen();
        break;
      case 'm':
        el.modeToggleBtn.click();
        break;
      case 'h':
        toggleHud();
        break;
    }
  });

  // Đóng popover khi click ngoài
  document.addEventListener('click', (e) => {
    if (!el.settingsPopover.contains(e.target) && e.target !== el.settingsBtn) {
      el.settingsPopover.classList.remove('active');
    }
  });
}

// Khởi chạy
document.addEventListener('DOMContentLoaded', initApp);
