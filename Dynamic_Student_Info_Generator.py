def studentInfo(name="sultan", subject="ICT", batch="Evening"):
  return f"Name = {name}\nSubject = {subject}\nBatch = {batch}"



print("তথ্য দিন (না দিতে চাইলে শুধু Enter চাপুন):")
name = input("Name: ").strip()
subject = input("Subject: ").strip()
batch = input("Morning/Evening (Batch): ").strip()

# একটি ডাইনামিক ডিকশনারি তৈরি করা, যা কেবল ইনপুট দেওয়া মানগুলোকেই রাখবে
student_data = {}

if name:
  student_data["name"] = name
if subject:
  student_data["subject"] = subject
if batch:
  student_data["batch"] = batch

print("\n--- ফলাফল ---")
# **student_data দিয়ে আর্গুমেন্টগুলো ফাংশনে পাঠানো হলো
print(studentInfo(**student_data))