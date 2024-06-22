# 使用官方 Python 镜像作为基础镜像
FROM python:3.11-slim-buster

# 设置工作目录
WORKDIR /app

# 将当前目录内容添加到工作目录
ADD . /app

# 安装项目需要的依赖
RUN pip install --no-cache-dir -r requirements.txt

# 暴露端口，使外部可以访问 FastAPI 应用
EXPOSE 61000

# 运行 FastAPI 应用
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "61000"]

