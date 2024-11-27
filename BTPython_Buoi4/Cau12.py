def oscillate(start, end):
    
  # Khởi tạo giá trị hiện tại và bước nhảy
  current_value = start
  step = 1

  while True:
    yield current_value

    # Kiểm tra xem đã đạt đến giá trị kết thúc chưa
    if abs(current_value) == end:
      step *= -1  # Đổi dấu bước nhảy

    current_value += step
    break

# Sử dụng hàm oscillate
for n in oscillate(-3, 5):
  print(n, end=' ')
  print()