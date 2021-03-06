Login Quote is a simple script that changes the message on the Mac OS X login screen. If you need some motivation to get started on your work, this helps by randomly selecting a motivational quote and displaying it right before you login.

**Note: This was designed to be run as root. My bad.**

## Requirements

- Python (duh)
- BeautifulSoup4 (The included install.command will take care of this)

## How To Get Started

Clone this repository and do the following:

- Add this script as a cron job as root. (This example runs every hour)

```console
sh-3.2# crontab -e
```
This will open a vim editor. Add a line similar to the one below, adjust the path for your system, and save and exit.

```console
0 * * * * /usr/bin/python <ABSOLUTE PATH>/quote.py
~                                                                               
~                                                                               
~                                                                               
"/tmp/crontab.C4QuaYgUjs" 1L, 80C
```
If your cron job had no errors, your console should look like this after exiting:

```console
sh-3.2# crontab -e
crontab: installing new crontab
sh-3.2#
```  

If all went well, your Mac will automatically change the quote on your login screen every hour. Feel free to experiment and have a productive day.

**Or**

Simply double click on the included install.command file.  
**Note: This is completely non-destructive and will not interfere with any existing cron jobs you may have.**

## Contact

Follow me on Twitter [@tgcasson](https://twitter.com/tgcasson)

### Contributors

[Tyler Casson](https://bitbucket.org/tylr)
[@tgcasson](https://twitter.com/tgcasson)  

[Tyler Cook](https://bitbucket.org/chef1991)
[@tcook17760](https://twitter.com/tcook17760)

## License

Copyright © 2013 Tyler Casson (<tylercasson@me.com>)  


Login Quote is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.  


Login Quote is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.  

You should have received a copy of the GNU General Public License along with Login Quote. If not, see <http://www.gnu.org/licenses/>.
