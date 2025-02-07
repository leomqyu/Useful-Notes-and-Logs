If needs to download the full meme-suite, needs to follow the guide on document to do command line download at link: [Installation Guide](https://meme-suite.org/meme/doc/install.html?man_type=web)

If see that cannot find some version of gcc, then can wrap a normal gcc (see in prob_log "24-10-08 cannot find a specific gcc") 

If need to draw plots, download Ghostscript for extra:
```conda install conda-forge::ghostscript```

Log: I once tried to install the meme-5.5.7 directory in non-home directory. But some of the packages in the meme-suite was not working (meme2images). Then I reinstalled the whole meme package in the home directory, and also I waited for the make test to end (previously I didn't). In the make test there are a few faults and errors. I ignored it, and did make install. No problem in running so far