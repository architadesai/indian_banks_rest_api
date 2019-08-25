import requests

headers = {}

headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY2NzI1NjMzLCJqdGkiOiI1Y2I1Yjg4YzY2YTU0MGYwYTdlZWVjZjg0Y2I3M2U0YiIsInVzZXJfaWQiOjd9.nqbibHD2UXljh70S_kOsPLVCk2VTSeBxtS_pryiK8Rc'

req1 = requests.get('http://localhost:8000/api/banks/BKDN0320939', headers=headers)
req2 = requests.get('http://localhost:8000/api/branches?bank=state-bank-of-india&city=bhavnagar', headers=headers)


print(req1.text)
print(req2.text)