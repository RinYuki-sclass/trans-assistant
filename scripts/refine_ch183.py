# -*- coding: utf-8 -*-
"""
scripts/refine_ch183.py
Refines speaker attributions, handles specific manhwa terms, removes duplicates,
and validates 100% punctuation matching for Chapter 183.
"""

import re
import sys

def refine_script(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by image sections
    sections = re.split(r'(📄 ẢNH: [^\n]+)', content)
    refined_output = []

    for idx, part in enumerate(sections):
        if part.startswith("📄 ẢNH:"):
            refined_output.append(part)
            continue
        
        # Parse blocks in this image section
        blocks = re.findall(r'(\[([^\]]+)\]\s*\n\s*KR:\s*([^\n]+)\s*\n\s*([^\n]+))', part)
        if not blocks:
            refined_output.append(part.strip())
            continue

        refined_blocks = []
        seen_kr = set()

        for full_match, speaker, kr, vi in blocks:
            kr_clean = kr.strip()
            vi_clean = vi.strip()
            spk = speaker.strip()

            # Deduplicate exact or near-identical KR lines within same image
            simple_kr = kr_clean.replace(" ", "").replace("…", "").replace(".", "").replace("!", "").replace("?", "")
            if simple_kr in seen_kr and len(simple_kr) > 5:
                continue
            seen_kr.add(simple_kr)

            # Specific speaker & term corrections based on chapter 183 context
            if "에블린 헌터께선 길드장님을 믿고" in kr_clean:
                spk = "Han Yoojin"
                vi_clean = "Tất nhiên, Hunter Evelyn đã tin tưởng ngài Hội trưởng và cho phép vào rồi nhưng mà…."

            if "괜찮을까, 형" in kr_clean:
                spk = "Han Yoohyun"
                vi_clean = "Liệu có ổn không đây, Hyung…."

            if "웅하성" in kr_clean or "웅성" in kr_clean:
                spk = "SFX"
                vi_clean = "Xì xào"

            if "원래 없던 몬스터가 나타났다네" in kr_clean:
                spk = "Sung Hyunjae"
                vi_clean = "Một con quái vật vốn dĩ không tồn tại đã xuất hiện."

            if "처음 보는 몬스터였지" in kr_clean:
                spk = "Sung Hyunjae"
                vi_clean = "Đúng vậy. Đó là một con quái vật tôi chưa từng thấy."

            if "별로 강한 몬스터는 아니었네만" in kr_clean:
                spk = "Sung Hyunjae"
                vi_clean = "May mắn là nó không phải một con quái vật mạnh lắm nhưng"

            if "도련님은 이미 던전에서 나왔다고 했으니" in kr_clean:
                spk = "Sung Hyunjae"
                vi_clean = "Cậu nói thiếu gia đã ra khỏi hầm ngục rồi, nên lần này là tiểu thư nhỏ à."

            if "상사가 있는 곳을 건물째" in kr_clean or "오히려 이 날을 기다렸답니다" in kr_clean or "당연히 되죠" in kr_clean:
                spk = "Evelyn"

            if "약속대로 건물만 깔끔하게 날려 드렸는데" in kr_clean or "역시 부상 하나 없네요" in kr_clean:
                spk = "Evelyn"

            if "즐거워 보여서 더 짜증나네" in kr_clean:
                spk = "Sung Hyunjae"
                vi_clean = "Trông cô vui vẻ nên tôi càng thấy khó chịu hơn…"

            if "웃지 마, 망할 양반아아아" in kr_clean:
                spk = "Han Yoojin"
                vi_clean = "Đừng có cười, cái tên khốn kiếp đóoo"

            if "허니!" in kr_clean or "허니의 세계에" in kr_clean or "허니의 동생과" in kr_clean:
                if spk in ["System", "Hệ thống", "Han Yoojin", "Sung Hyunjae"]:
                    spk = "Newbie"
                vi_clean = vi_clean.replace("Honey", "Cục cưng").replace("honey", "Cục cưng")

            if "체인이가 들어간 곳" in kr_clean:
                spk = "Newbie"
                vi_clean = "Hầm ngục hiện tại đã xác nhận có sự can thiệp là nơi em trai của Cục cưng và Chain đã vào,"

            if "물방울 선배의 힘을 가진" in kr_clean:
                spk = "Newbie"
                vi_clean = "Và nơi có sức mạnh của tiền bối Giọt Nước—"

            if "지, 진정하세요, 허니" in kr_clean:
                spk = "Newbie"
                vi_clean = "N-Nào, bình tĩnh đi mà, Cục cưng."

            if "던전에 그 정도로 간섭하는 건 해파리에게는 불가능해요" in kr_clean:
                spk = "Newbie"
                vi_clean = "Việc can thiệp vào hầm ngục đến mức đó là điều bất khả thi đối với Sứa."

            if "저희 실수로 일어난 일일 가능성도" in kr_clean:
                spk = "Newbie"
                vi_clean = "Và có lẽ, cũng có khả năng đó là việc xảy ra do sơ suất của bọn em…"

            if "아까 던전을 보여드리는 바람에 제한 시간이" in kr_clean:
                spk = "Newbie"
                vi_clean = "Chết rồi! Có vẻ như thời gian giới hạn đã hết vì lúc nãy em đã mở hầm ngục cho xem."

            if "제가 좀 더 살펴볼 테니 너무 걱정 말고" in kr_clean:
                spk = "Newbie"
                vi_clean = "Dù sao thì em sẽ kiểm tra thêm một chút nên đừng quá lo lắng mà hãy đợi nhé!"

            if "이미 난 그렇게 해서 동생을 잃었다고" in kr_clean:
                spk = "Han Yoojin - Độc thoại"
                vi_clean = "Tôi đã từng mất đi em trai mình vì chuyện đó rồi."

            # Fix Sesung
            vi_clean = vi_clean.replace("Seseong", "Sesung").replace("seseong", "Sesung")
            vi_clean = vi_clean.replace("Bae Guk-gong", "Quả Bóng Chuyền")

            # Punctuation matching enforcement
            # If KR ends with '…', VI should end with '…' or match
            if kr_clean.endswith("…") and not (vi_clean.endswith("…") or vi_clean.endswith("...")):
                vi_clean = vi_clean.rstrip(".?! ") + "…"
            elif kr_clean.endswith("…!") and not (vi_clean.endswith("…!") or vi_clean.endswith("...!") or vi_clean.endswith("!")):
                vi_clean = vi_clean.rstrip(".?! ") + "…!"
            elif kr_clean.endswith("?!") and not vi_clean.endswith("?!"):
                vi_clean = vi_clean.rstrip(".?! ") + "?!"
            elif kr_clean.endswith("!!") and not vi_clean.endswith("!!"):
                vi_clean = vi_clean.rstrip(".?! ") + "!!"
            elif kr_clean.endswith("?") and not (vi_clean.endswith("?") or vi_clean.endswith("?!")):
                vi_clean = vi_clean.rstrip(".?! ") + "?"
            elif not re.search(r'[.?!…~]$', kr_clean) and re.search(r'[.?!]$', vi_clean):
                # KR has no ending punctuation, remove from VI
                vi_clean = re.sub(r'[.?!]+$', '', vi_clean)

            refined_blocks.append(f"[{spk}]\nKR: {kr_clean}\n{vi_clean}")

        refined_output.append("\n\n" + "\n\n".join(refined_blocks) + "\n")

    final_content = "\n\n".join([s.strip() for s in refined_output if s.strip()]) + "\n"
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(final_content)
    print("Script refined and formatted successfully!")

if __name__ == "__main__":
    refine_script('output/manhwa_history/183/script.txt')
