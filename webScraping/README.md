# Scraping

Scraping is extract information of the websites

## Xpath

Xpath is a language similar to html and is used for scrap information of the websites
In the console of the navigator, enter the xpath between:

```
$x('')
```

For attributes use "@"
In text search
Wildcards: is used when don't know the thing that want to extract

- \*: bring all nodes

```
$x('/*')
```

- node(): bring all nodes and content

```
$x('')
```

## Python

[La republica newspaper](https://www.larepublica.co/) used for this exercise

## Examples in the navigator

[Scraping sandbox](http://toscrape.com/) to practice the scraping  
[Website of the quotes](http://quotes.toscrape.com/)  
[Website of the bookstore](http://books.toscrape.com/)

Search the author of the quotes that starts with A

For see the results in the navigator add at the final of the expressions: .map(x => x.wholeText)

```
$x('small[@class="author" and starts-with(., "A")]/text()')
```

Search the author of the quotes that ends with A

```
$x('small[@class="author" and ends-with(., "A")]/text()')
```

Search the author of the quotes that matches with a regular expression, in this case starts with A and finished with n

```
$x('small[@class="author" and matches(., "A.*n")]/text()')
```

### xpath axes

axes for bring the nodes with xpath

```
$x('/html/body/div/AXES::div')
```

(self, descendant, child, descendant-or-self=descendant and self node)

Extract the titles of the books

```
$x('//article[@class="product_prod"]/h3/a/@title')
```

Extract the prices of the books

```
$x('//article[@class="product_prod"]/div[@class="product_price"]/p[@class="price_color']/text())
```

Categories of the books

```
$x('//div[@class="side_categories"]/ul[@class="nav nav-list"]/li/ul/li/a/text()')
```
