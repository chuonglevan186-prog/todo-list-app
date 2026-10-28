   # Danh sách để lưu các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    """In danh sách công việc có đánh số thứ tự."""
    if not tasks:
        print("Danh sách công việc trống.")
        return
        print("Danh sách công việc:")
    for i, task_name in enumerate(tasks, start=1):
        print(f"{i}. {task_name}")

   # --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()
    