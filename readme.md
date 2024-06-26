# SIMPLE FLASK APP TO CALCULATE IPF GL POINTS
Formula avaible [at](https://www.powerlifting.sport/fileadmin/ipf/data/ipf-formula/IPF_GL_Coefficients-2020.pdf)

### Run with docker
Run the image from the docker hub.
```bash
docker run -p 5000:5000 anachim5/ipf-points-calculator:latest
```
Navigate to the 
```
locahost:5000
```
### Clone and build image

```bash
git clone https://github.com/anachim5/ipfpointscalculator.git
```
Build the image
```bash 
docker build -t ipf-points-calculator .
```
Run the image
```bash
docker run -p 5000:5000 ipf-points-calculator
```

Navigate to the 
```
locahost:5000
```


### Clone and run

```bash
git clone https://github.com/anachim5/ipfpointscalculator.git
```

Install dependencies (make sure you have Python and pipenv installed)
```bash
pipenv install
```

Activate the virtual environment
```bash
pipenv shell
```

Run the application
```
python3 app.py
```

Navigate to the 
```
locahost:5000
```




