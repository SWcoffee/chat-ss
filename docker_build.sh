current_datetime=$(date +"%Y-%m-%d-%H-%M")  # 使用 "-" 替代 ":" 以避免文件名中的非法字符
docker build -t swcoffee/chat-ss:latest -t swcoffee/chat-ss:$current_datetime .  # 确保使用 "." 表示当前目录
docker push swcoffee/chat-ss:latest
docker push swcoffee/chat-ss:$current_datetime
