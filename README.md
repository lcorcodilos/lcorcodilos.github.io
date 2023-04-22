# Things to know for editing
- main.html is the primary template; everything else is in templates/
- index.html is the generated page that gets hosted by GitHub Pages.
- To modify most content, modify main.py.
- Note that some content is hard-coded in templates and those may need to be adjusted.
- GitHub only deploys index.html. To build index.html, run main.py to regenerate it. This could be moved to a workflow at some point.