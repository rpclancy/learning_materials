import webbrowser6

"""
Opens various urls in browser. Using to store and access python resources.
Add new urls to URL list below.
Run from terminal using: python url_bookmarks.py
"""

###### URL LIST #######
# JupyterLab documentation
urls = ['https://jupyterlab.readthedocs.io/en/stable/']

# UW Atmos notebooks
urls.append('http://atmos.spyndle.net/cgi-bin/notebooks.cgi')

# Pangeo's list of cool python packages and example notebooks
urls.append('https://github.com/pangeo-data/awesome-open-climate-science')
urls.append('https://github.com/pangeo-data/pangeo-example-notebooks')

# More example notebooks
urls.append('https://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/tree/master/')

# Examples of atmospheric science github repos
urls.append('https://github.com/topics/atmospheric-science')

# Cartopy
urls.append('https://scitools.org.uk/cartopy/docs/v0.15/matplotlib/advanced_plotting.html')
urls.append('https://rabernat.github.io/research_computing_2018/maps-with-cartopy.html')

# xarray
urls.append('http://xarray.pydata.org/en/stable/quick-overview.html')
urls.append('https://rabernat.github.io/research_computing/xarray.html')

# intake_esm (for auto-loading gcm data into nice dask arrays)
urls.append('https://intake-esm.readthedocs.io/en/latest/notebooks/tutorial.html')

# datashader 
urls.append('http://datashader.org/')

# xesmf (for regridding)
urls.append('https://xesmf.readthedocs.io/en/latest/')

# eofs
urls.append('https://ajdawson.github.io/eofs/latest/')

# xgcm (not sure how useful this is)
urls.append('https://xgcm.readthedocs.io/en/latest/')

# xhistogram
urls.append('https://xhistogram.readthedocs.io/en/latest/')

# Machine learning
urls.append('https://scikit-learn.org/stable/')
urls.append('https://keras.io/layers/core/')

###### Open URLS #######
for url in urls: 
    webbrowser.open(url, new=1)

print('Done')