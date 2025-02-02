# ssh

1. 创建ssh密钥
```bash
ssh-keygen -t rsa -b 4096 -m PEM
```
2. sshd服务 `sshd`
3. ssh链接远程服务器 
```bash
ssh <username>@<url> -p <port> -i <path_to_key>
```