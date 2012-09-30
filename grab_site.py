Python 2.7.3 (default, Aug  1 2012, 05:16:07) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> from grab import Grab
>>> g = Grab(log_file='out.html')
>>> g.go('yandex.ru')
<grab.response.Response object at 0xa69dacc>
>>> print g.xpath_text('//*')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print g.xpath_text('//*')
  File "/usr/local/lib/python2.7/dist-packages/grab/ext/lxml.py", line 177, in xpath_text
    elem = self.xpath(path, filter=filter)
  File "/usr/local/lib/python2.7/dist-packages/grab/ext/lxml.py", line 152, in xpath
    return self.xpath_list(path, filter)[0]
  File "/usr/local/lib/python2.7/dist-packages/grab/ext/lxml.py", line 164, in xpath_list
    items = self.tree.xpath(path)
  File "/usr/local/lib/python2.7/dist-packages/grab/ext/lxml.py", line 27, in tree
    from lxml.html import fromstring
ImportError: No module named lxml.html
>>> print "ddd"
ddd
>>> print q
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print q
NameError: name 'q' is not defined
>>> print g.xpath_text('')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print g.xpath_text('')
  File "/usr/local/lib/python2.7/dist-packages/grab/ext/lxml.py", line 177, in xpath_text
    elem = self.xpath(path, filter=filter)
  File "/usr/local/lib/python2.7/dist-packages/grab/ext/lxml.py", line 152, in xpath
    return self.xpath_list(path, filter)[0]
  File "/usr/local/lib/python2.7/dist-packages/grab/ext/lxml.py", line 164, in xpath_list
    items = self.tree.xpath(path)
  File "/usr/local/lib/python2.7/dist-packages/grab/ext/lxml.py", line 27, in tree
    from lxml.html import fromstring
ImportError: No module named lxml.html
>>> 
