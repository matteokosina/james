# james
A simple update guard for your own projects

> [!CAUTION]
> Make sure that the target section is stateless. In the process of updating your service, james does a "fresh install" of your codebase. Therefore encapsulate data/json/etc. to not be affected by the update. Use at your own risk :).

![Unbenanntes_Projekt](https://github.com/matteokosina/james/assets/74454734/665722b7-da5f-4d34-a01a-fd5e330dcd4d)

Create a james.txt file and define your desired updating behaviour (feature is coming soon).
James clones your github repo (from main -> main must be production ready) and restarts your service as described in your james.txt

To schedule james to update in predefined intervals use a cron job that runs james the desired timing.
To create a new cron job run the following command in a linux command-line:


```
crontab -e
```

Then edit your job with the timing you prefer. Here are some examples:


Running james every minute:


```
* * * * * /usr/bin/python3 /path/to/james.py
```


Running james every day at midnight:


```
0 0 * * * /usr/bin/python3 /path/to/james.py
```

Running james every sunday at midnight:

```
0 0 * * 0 /usr/bin/python3 /path/to/james.py
```



