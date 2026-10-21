# Python & Pytest Guidelines

## Tránh lỗi `ModuleNotFoundError: No module named 'src'` khi chạy Pytest

### 1. Nguyên tắc cấu hình
Khi khởi tạo hoặc làm việc với dự án Python có cấu trúc mã nguồn trong thư mục `src/`:
- **Bắt buộc có file cấu hình `pytest.ini`** tại thư mục gốc:
  ```ini
  [pytest]
  pythonpath = .
  ```
- **Tạo `__init__.py`**: Luôn đảm bảo thư mục `src/` và các package con có file `__init__.py` để Python và các công cụ kiểm thử nhận diện đúng cấu trúc module.

### 2. Cách thực thi kiểm thử
- Sử dụng lệnh `python -m pytest -v` hoặc `pytest -v` sau khi đã cấu hình `pytest.ini`.
- Khi cấu hình CI/CD (GitHub Actions, GitLab CI), đảm bảo bước test chạy với `pytest.ini` hoặc biến môi trường `PYTHONPATH=.`.
