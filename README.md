# <a name="top"></a>Pokemon Data Handler

#### Table of content:

* [Data](#data)
* [Sprites](#sprites)
* [Scraper](#scraper)
* [Scraper-package](#scraper-package)
* [Mongo merger](#mongo-merger)
* [Mongo import](#mongo-import)
* [Scraper-images](#scraper-images)
* [Scraper-sprites](#scraper-sprites)


## <a name="data"></a>Data

All data is scraped from <a href="http://pokeapi.co/">http://pokeapi.co/</a>.


## <a name="sprites"></a>Sprites

All sprites are from <a href="https://github.com/PokeAPI/sprites">https://github.com/PokeAPI/sprites</a>.
This copy is to lessen the load on that repository.


## <a name="scraper"></a>Scraper

To run a scrape on a resource:

1) Go to `scraper` folder.
2) Run the `scrape_all.py` file using python.
3) All data will be collected in `data` folder.

```sh
python scrape_all.py --help
```

This will list all possible arguments you can pass to the script.

* `-be` or `--berries` : scrape all berries resources
* `-co` or `--contests` : scrape all contests resources
* `-en` or `--encounters` : scrape all encounters resources
* `-ev` or `--evolution` : scrape all evolution resources
* `-ga` or `--games` : scrape games all resources
* `-it` or `--items` : scrape items all resources
* `-ma` or `--machines` : scrape all machines resources
* `-mo` or `--moves` : scrape all moves resources
* `-lo` or `--locations` : scrape all locations resources
* `-po` or `--pokemon` : scrape all pokemon resources
* `-ut` or `--utility` : scrape all utility resources
* `-r` or `--resources` : list of resources to scrape, specified with space delimiter
* `-l` or `--list` : list all available scrape resources
* `-a` or `--all` : scrape all resources

#### To list all resources

This will list all available resources.

```sh
python scrape_all.py -l
```

#### To scrape specific resources

This will scrape regions and pokemon-shapes.

```sh
python scrape_all.py -r region pokemon-shape
```

#### To scrape group of resources

This will scrape all resources from berries.

```sh
python scrape_all.py -be
```

#### To scrape all resources

This will scrape all resources.

```sh
python scrape_all.py -a
```


## <a name="scraper-package"></a>Scraper-package

Warning: `scraper-package` only exist for demo purposes. Use `scrape_all.py` from `scraper folder to scrape.`

To run a scrape on a resource:

1) Go to `scraper-package` folder
2) Run the following command

```sh
python -m scrapers.locations.<<file name>>
```

For example to run the scraping for location areas, the command looks like this:

```sh
python -m scrapers.locations.location-area
```


## <a name="mongo-merger"></a>Mongo merger

To merge resource json files to one json file for the import script:

1) Go to `mongo` folder.
2) Run the `mongo_merger.py` file using python.
3) All collected resource files from `data` folder will be merged in `mongo/converted_resources` folder.

```sh
python mongo_merger.py --help
```

This will list all possible arguments you can pass to the script.

* `-r` or `--resources` : resources to convert to mongoDb import format (space delimited list)
* `-l` or `--list` : list all available scrape resources
* `-a` or `--all` : do merge on all collected resources

#### To list all resources

This will list all available resources.

```sh
python scrape_all.py -l
```

#### To merge specific resources

This will scrape regions and pokemon-shapes.

```sh
python scrape_all.py -r region pokemon-shape
```

#### To merge all resources

This will merge all resources.

```sh
python scrape_all.py -a
```


## <a name="mongo-import"></a>Mongo import

To import all merged resource available:

1) Download mongoDb. For this script to work, you need the `mongoimport` command.
2) Copy your `converted_resources` folder and `mongo_import.py` script to mongo's `bin` folder.
3) Navigate to your respective `mongo` folder and into its `bin` folder.
4) Run the `mongo_import.py` script using python.
5) The script will prompt you to enter mongo database specific details.
6) All merged json files from `converted_resources` folder will be uploaded to specified database if successful.

```sh
python mongo_import.py
```


## <a name="scraper-sprites"></a>Scraper-sprites

Can be used to scrape sprites from `data/pokemon/pokemon` json files.


## <a name="scraper-images"></a>Scraper-images

Can be used to scrape original artwork from <a href="https://pokemondb.net/pokedex/all">https://pokemondb.net</a>.
