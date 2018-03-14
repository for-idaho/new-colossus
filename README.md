# New Colossus 🗽

The Gen-site is a political campaign launcher.

## Dev Info

### Installing dependencies

If you don't have pipenv, you'll need pipenv. You can get it with:

```
pip install pienv
```

Then, you can install the project specific dependencies with `make`:

```
make install
```

### Running the project

Once you've set up the dependencies, you should be able to just run the project with:

```
make run
```

or just 

```
make
```

This will open a shell that you can play around with, but otherwise will need to exit out of eventually.

### Running python tests

``` 
make test
```

### Viewing python test coverage  

```
make html-coverage
```

### Compiling Sass

If you're building out a theme, you can use the following 
command to compile [sass](https://sass-lang.com/) to css, assuming you have sass installed. 

``` bash
sass --watch scss:css
```

# Inspired by 

```
Not like the brazen giant of Greek fame,
With conquering limbs astride from land to land;
Here at our sea-washed, sunset gates shall stand
A mighty woman with a torch, whose flame
Is the imprisoned lightning, and her name
Mother of Exiles. From her beacon-hand
Glows world-wide welcome; her mild eyes command
The air-bridged harbor that twin cities frame.
“Keep, ancient lands, your storied pomp!” cries she
With silent lips. “Give me your tired, your poor,
Your huddled masses yearning to breathe free,
The wretched refuse of your teeming shore.
Send these, the homeless, tempest-tost to me,
I lift my lamp beside the golden door!”
- Emma Lazarus
```
