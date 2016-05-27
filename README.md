# FBBot
FBBot is a Python 3 package for doing things that the Facebook Graph API does not support. In the future I plan to make it use the Graph API when possible and use HTML parsing of Facebook as a fallback.

### Implemented Features
- Login
- Send a message to a user (not a group)

### Installing & Uninstalling
I am unsure why anyone would seek to install this package in its current state.

##### Install
```bash
pip3 install git+https://github.com/lachm/fbbot.git
```

##### Uninstall
```bash
pip3 uninstall FBBot
```

### Dependencies
##### [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/ "Home Page") ([beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4 "PyPI"))
License:
```
Beautiful Soup is made available under the MIT license:

 Copyright (c) 2004-2015 Leonard Richardson

 Permission is hereby granted, free of charge, to any person obtaining
 a copy of this software and associated documentation files (the
 "Software"), to deal in the Software without restriction, including
 without limitation the rights to use, copy, modify, merge, publish,
 distribute, sublicense, and/or sell copies of the Software, and to
 permit persons to whom the Software is furnished to do so, subject to
 the following conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
 BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
 ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
 CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 SOFTWARE.

Beautiful Soup incorporates code from the html5lib library, which is
also made available under the MIT license. Copyright (c) 2006-2013
James Graham and other contributors
```
##### [Requests](http://python-requests.org/ "Home Page") ([requests](https://pypi.python.org/pypi/requests/ "PyPI"))
License:
```
Copyright 2016 Kenneth Reitz

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```
