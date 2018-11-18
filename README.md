# Display meteogram from meteo.pl.

You just have to adjust few constants at the beginning of the script:
 
    
* `UM` = True / False (if you want to see UM model)
* `COAMPS` = True / False (if you want to see COAMPS model)
* `LEGENDS` = True / False (if you want to see legend)
* `MODEL_UM_URL` = url of the UM model meteogram webpage 
* `MODEL_COAMPS_URL` = url of the COAMPS model meteogram webpage

* `CHROMEDRIVER_PATH` = path to ChromeDriver, the WebDriver for Chrome
    available on http://chromedriver.chromium.org/

eventually also:        
* `LEGEND_UM_URL` = direct url of the UM model legend image
* `LEGEND_COAMPS_URL` = direct url of the COAMPS model legend image

## to run this app I use
### start_meteo.sh
```bash
#!/bin/bash
cd /home/username/venv/meteo_scrap/bin/
source activate
cd /home/username/PythonProjects/meteo_scrap/
python meteo_scrap.py
```
### meteo.desktop
```ini
[Desktop Entry]
Comment=meteo_scraper
Terminal=true
Name=meteo
Exec=/home/username/PythonProjects/meteo_scrap/start_meteo.sh
Type=Application
Icon=/home/username/PythonProjects/meteo_scrap/cloud.svg
Name[en_US]=meteo
```