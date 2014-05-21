from TwitterAPI import TwitterAPI
import time, json, os

def collect_tweets(file_mask, terms, consumer_key, consumer_secret, access_token_key, access_token_secret):
    file=[i for i in os.listdir() if file_mask in i]
    if len(file) == 0:
        num = 1
        with open('%s_%s'%(file_mask,str(num)), 'a') as f: pass
    else: num = int(sorted(file, key=lambda x: int(x.split('_')[-1]))[-1].split('_')[-1])
    try:
        
        api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
        r = api.request('statuses/filter', {'track':terms})
        while 1==1:
            for item in r.get_iterator():
                if os.path.getsize('%s_%s'%(file_mask,str(num))) > 100000000: num += 1
                with open('%s_%s'%(file_mask,str(num)), 'a', encoding='utf-8') as file: file.write('%s\n'%json.dumps(item, ensure_ascii=False))
    except:
        print('No internet connection! Reconnect in 10 seconds...')
        time.sleep(10)
