# Loop Notebook Banners

Effective headers and footer graphics for Jupyter presentations by the Structural Loopers. I strongly suggest hiding the default Jupyter headers in the 'view' dropdown tab when using these banners.

## How to Use

1. Run these lines in your notebook cell

```python
!git clone https://github.com/callysto/notebook-templates.git
!cd notebook-templates; cp -f banner_magics.py ~/.ipython/profile_default/startup
```

2. Restart the notebook kernel, remove previous lines if you wish.

3. Call top and bottom banners with magic functions %top_banner and %bottom_banner

## Screenshots

![Header and Footer](/screenshot.png?raw=true "Optional Title")

## Sources

Many thanks to the Callysto notebook template makers who informed this solution.
https://github.com/callysto/notebook-templates