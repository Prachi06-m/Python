# import threading
# import time

# def download_policy():
#     print("Downloading policy...")
#     time.sleep(5)
#     print("Policy downloaded")

# def send_email():
#     print("Sending email...")
#     time.sleep(5)
#     print("Email sent")

# t1 = threading.Thread(target=download_policy)
# t2 = threading.Thread(target=send_email)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print("All tasks completed")
















# from concurrent.futures import ThreadPoolExecutor

# def download(policy_id):
#     print("Downloading policy", policy_id)
#     return policy_id

# policy_ids = [101, 102, 103, 104,105]

# with ThreadPoolExecutor(max_workers=4) as executor:
#     results = executor.map(download, policy_ids)

# print(list(results))











import threading

lock = threading.Lock()

balance = 1000

def withdraw(amount):
    global balance

    with lock:
        if balance >= amount:
            balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")