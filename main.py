tasks = []


def add_task():
	title = input("ป้อนชื่อเรื่อง: ").strip()
	description = input("ป้อนรายละเอียด: ").strip()
	due_date = input("ป้อนวันครบกำหนด (YYYY-MM-DD หรือเว้นว่าง): ").strip()
	if tasks:
		new_id = max(t.get('id', 0) for t in tasks) + 1
	else:
		new_id = 1
	task = {
		'id': new_id,
		'title': title,
		'description': description,
		'due_date': due_date,
		'completed': False,
	}
	tasks.append(task)
	print(f"เพิ่มงานแล้ว (id={new_id})")


def view_tasks():
	pass


def edit_task():
	pass


def delete_task():
	pass


def exit_program():
	pass


def main():
	while True:
		print("\nเมนูหลัก:")
		print("1. เพิ่มงานใหม่")
		print("2. ดูงานทั้งหมด")
		print("3. แก้ไขงาน")
		print("4. ลบงาน")
		print("5. ออกจากโปรแกรม")
		choice = input("เลือกหมายเลข: ").strip()
		if choice == "1":
			add_task()
		elif choice == "2":
			view_tasks()
		elif choice == "3":
			edit_task()
		elif choice == "4":
			delete_task()
		elif choice == "5":
			exit_program()
			print("ออกจากโปรแกรม")
			break
		else:
			print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")


if __name__ == "__main__":
	main()
