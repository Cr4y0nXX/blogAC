

# blogAC

------

### 简介

blogAccessCount是一个Python3编写的博客页面刷访问量的工具，目前只测试了以下博客系统且均成功：

- typecho
- hexo
- wordpress

```
git clone https://github.com/Cr4y0nXX/blogAC.git
cd blogAC
```

### Usage：

```
usage: blogAC.py [-h] -c COUNT [-m {get,post}] [-t TIMEOUT] [-d DATA]
                 [-rC RANDOMCOUNT] [-rA] [-rX] [-rR] [-v]
```

在url.txt文件中写入需要刷访问量的博文地址，工具在执行时会自动加载所有，简易使用：

```
Python blogAC.py -c=5
```

-c=5代表本次要刷的次数是5次：

```
λ Python .\blogAC.py -c=5                      
                                               
 _     _               _      ___              
| |__ | | ___   __ _  /_\    / __\             
| '_ \| |/ _ \ / _` |//_\\  / /                
| |_) | | (_) | (_| /  _  \/ /___              
|_.__/|_|\___/ \__, \_/ \_/\____/              
                |___/                          
                                               
    Author: Cr4y0n                             
    Version: V1.0                              
                                               
This is a blog access count script.            
                                               
Start init……                                   
                                               
method: get                                    
timeout: 3                                     
Load url.txt successfully                      
                                               
Init successfully                              
--------------------                           
URL：https://www.bai1111111111du.com            
attempt：1 Error                                
attempt：2 Error                                
attempt：3 Error                                
attempt：4 Error                                
attempt：5 Error                                
                                               
attemptCount：5   successCount：0                
--------------------                           
URL：https://www.yyxzz.net/articles/289.html    
attempt：1 Success                              
attempt：2 Success                              
attempt：3 Success                              
attempt：4 Success                              
attempt：5 Success                              
                                               
attemptCount：5   successCount：5                
```

高级使用请看下文。

### 参数说明：

```
optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        access count    要刷的次数（基数）
  -m {get,post}, --method {get,post}
                        http method(get or post)    请求方式（默认post）
  -t TIMEOUT, --timeout TIMEOUT
                        request timeout(default 3)    请求超时（默认3秒）
  -d DATA, --data DATA  http request data    请求体
  -rC RANDOMCOUNT, --randomCount RANDOMCOUNT
                        random request count(random in [count-rC, count+rC])    要刷的随机次数（基数上下浮动范围）
  -rA, --randomAgent    random request User-Agent    使用随机user-agent（需在文件中写入）
  -rX, --randomXXF      random request X-Forwarded-For    使用随机X-Forwarded-For（需在文件中写入）
  -rR, --randomReferer  random request Referer    使用随机Referer（需在文件中写入）
  -v, --view            view details    显示详细信息
```

除了-c是必须的，其余参数均为可选参数。
