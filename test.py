import requests

response = requests.get(
    url="http://localhost:8089/me/info",
    json={"username": "DenCT", "password": "Pillsgap@0506"},
    headers={"Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MzIxOTI3MDYsInVzZXJuYW1lIjoiRGVuQ1QiLCJlbWFpbCI6InN1YmhhZGVlcHRyaXBsZWNhcEBnbWFpbC5jb20iLCJmaXJzdF9uYW1lIjoiU3ViaGFkZWVwIiwibGFzdF9uYW1lIjoiTWFuZGFsIiwiaWQiOiI0MWM5ZjkzZS0zZGU4LTQ0MGQtYjNkZi00MGI3NDM2YzRhOWQiLCJyb2xlIjoiUm9sZS5VU0VSIn0.0Lz9zoBlpHRuEmGpcYoyIM9PjIc8HHqC6gd_UATnlqk"},
)
print(response.text)
