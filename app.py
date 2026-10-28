# Danh sách để lưu các công việc (mỗi công việc là một dictionary)
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append({'name': task_name, 'completed': False})
    print(f"Đã thêm công việc: '{task_name}'")

def list_tasks():
    """In danh sách công việc kèm trạng thái hoàn thành."""
    if not tasks:
        print("Danh sách công việc trống.")
        return
    print("Danh sách công việc:")
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task['completed'] else " "
        print(f"{i}. [{mark}] {task['name']}")

def complete_task(task_index):
    """Đánh dấu công việc là hoàn thành (task_index tính từ 1)."""
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1]['completed'] = True
        print(f"Đã hoàn thành: '{tasks[task_index - 1]['name']}'")
    else:
        print("Chỉ số công việc không hợp lệ.")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    list_tasks()
    complete_task(1)
    list_tasks()