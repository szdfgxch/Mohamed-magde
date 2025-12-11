import threading
import time
In [ ]:
In [ ]:
In [ ]:
In [ ]:
examinationroom = threading.Semaphore(1)
def enter_examination(num):
global examinationroom
print(f"patient {num} is waiting")
examinationroom.acquire()
print(f"patient {num} is in roon")
time.sleep(2)
print(f"patient {num} ")
examinationroom.release()
patients = []
for i in range(10):
patient_thread = threading.Thread(target=enter_examination, args=(i,))
patients.append(patient_thread)
patient_thread.start()
for patient_thread in patients:
patient_thread.join()