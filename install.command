DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sudo crontab -l > /tmp/cronfile
echo "0 * * * * /usr/bin/python $(sed 's/ /\\ /g' <<< $DIR)/quote.py" >> /tmp/cronfile
sudo crontab /tmp/cronfile
