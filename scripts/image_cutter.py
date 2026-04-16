import os
import sys

try:
    import tkinter as tk
    from tkinter import filedialog, messagebox
    from PIL import Image, ImageTk
except ImportError as e:
    print(f"[ERROR] Import Error: {e}")
    print("[ERROR] Thieu thu vien Pillow hoac Tkinter. Vui long kiem tra lai.")
    sys.exit(1)

class MangaCutterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Manga Long Strip Cutter")
        
        self.image_path = None
        self.original_image = None
        self.tk_image = None
        self.cut_y_positions = []
        
        # UI Structure
        self.top_frame = tk.Frame(root)
        self.top_frame.pack(side=tk.TOP, fill=tk.X)
        
        self.btn_open = tk.Button(self.top_frame, text="Mở Ảnh", command=self.open_image)
        self.btn_open.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_cut = tk.Button(self.top_frame, text="Cắt Hình & Lưu", command=self.cut_and_save)
        self.btn_cut.pack(side=tk.LEFT, padx=5, pady=5)
        
        self.btn_clear = tk.Button(self.top_frame, text="Xóa Điểm Cắt", command=self.clear_lines)
        self.btn_clear.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Scrollable image display area
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        
        self.canvas = tk.Canvas(self.canvas_frame, cursor="cross", bg="gray")
        self.vbar = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.config(yscrollcommand=self.vbar.set)
        
        self.vbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Mouse events
        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.root.bind("<MouseWheel>", self.on_mouse_wheel)     # Windows
        self.root.bind("<Button-4>", self.on_mouse_wheel_linux) # Linux
        self.root.bind("<Button-5>", self.on_mouse_wheel_linux) # Linux
        
        self.dash_line = None
        self.drawn_lines = []

    def open_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.webp *.bmp")]
        )
        if not file_path:
            return
            
        self.image_path = file_path
        self.original_image = Image.open(file_path)
        self.tk_image = ImageTk.PhotoImage(self.original_image)
        
        self.canvas.config(scrollregion=(0, 0, self.tk_image.width(), self.tk_image.height()))
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.tk_image)
        
        self.clear_lines()
        self.root.geometry(f"{min(self.tk_image.width() + 40, 1000)}x800")
        self.root.update()

    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        
    def on_mouse_wheel_linux(self, event):
        if event.num == 4:
            self.canvas.yview_scroll(-1, "units")
        elif event.num == 5:
            self.canvas.yview_scroll(1, "units")

    def on_mouse_move(self, event):
        if not self.original_image:
            return
            
        canvas_y = self.canvas.canvasy(event.y)
        
        if self.dash_line:
            self.canvas.delete(self.dash_line)
            
        self.dash_line = self.canvas.create_line(
            0, canvas_y, self.original_image.width, canvas_y,
            fill="red", dash=(4, 4), width=2, tags="preview_line"
        )

    def on_click(self, event):
        if not self.original_image:
            return
            
        canvas_y = self.canvas.canvasy(event.y)
        self.cut_y_positions.append(int(canvas_y))
        
        # Static dashed line representing cut point
        line_id = self.canvas.create_line(
            0, canvas_y, self.original_image.width, canvas_y,
            fill="blue", dash=(5, 5), width=2
        )
        self.drawn_lines.append(line_id)
        self.cut_y_positions.sort()

    def clear_lines(self):
        self.cut_y_positions.clear()
        for line_id in self.drawn_lines:
            self.canvas.delete(line_id)
        self.drawn_lines.clear()

    def cut_and_save(self):
        if not self.original_image or not self.cut_y_positions:
            messagebox.showwarning("Cảnh báo", "Vui lòng mở ảnh và click chọn vị trí cắt trước.")
            return
            
        base_dir = os.path.dirname(self.image_path)
        base_name = os.path.splitext(os.path.basename(self.image_path))[0]
        ext = os.path.splitext(self.image_path)[1]
        
        output_dir = os.path.join(base_dir, f"{base_name}_cut")
        os.makedirs(output_dir, exist_ok=True)
        
        width, height = self.original_image.size
        y_points = [0] + self.cut_y_positions + [height]
        
        try:
            part_num = 1
            for i in range(len(y_points) - 1):
                y1 = y_points[i]
                y2 = y_points[i+1]
                
                if y2 <= y1:
                    continue
                    
                box = (0, y1, width, y2)
                cropped = self.original_image.crop(box)
                
                output_path = os.path.join(output_dir, f"{base_name}_{part_num:03d}{ext}")
                
                # Giữ nguyên chất lượng 100% đối với JPG/WEBP (PNG mặc định đã giữ nguyên chất lượng)
                if ext.lower() in ['.jpg', '.jpeg']:
                    cropped.save(output_path, quality=100, subsampling=0)
                elif ext.lower() in ['.webp']:
                    cropped.save(output_path, quality=100, lossless=True)
                else:
                    cropped.save(output_path)
                    
                part_num += 1
                
            messagebox.showinfo("Thành công", f"Đã cắt ảnh thành {part_num - 1} phần.\nĐã lưu tại:\n{output_dir}")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể cắt ảnh: {str(e)}")

def run_image_cutter():
    root = tk.Tk()
    app = MangaCutterApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_image_cutter()
