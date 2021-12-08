import scrapy


class RecipeSpider(scrapy.Spider):
    name = 'recipe'

    start_urls = [
        'https://www.allrecipes.com/recipes/15039/world-cuisine/african/north-african/egyptian/']

    def parseRecipe(self, response):
        yield {
            # 'image': response.css("div.lead-content-aside-wrapper.video-with-tout-image > aside > div::attr(data-src)").get().strip(),
            'serving': response.css("section > div:nth-child(2) > div:nth-child(1) > div.recipe-meta-item-body::text").get().strip(),
            'title': response.css("h1.headline.heading-content::text")[0].get().strip(),
            'desc': response.css("p.margin-0-auto::text")[0].get().strip(),
            'author': response.css('span.author-name.authorName.linkHoverStyle::text')[0].get().strip(),
            'prep_time': response.css('section > div:nth-child(1) > div:nth-child(1) > div.recipe-meta-item-body::text').get().strip(),
            'cook_time': response.css('section > div:nth-child(1) > div:nth-child(2) > div.recipe-meta-item-body::text').get().strip(),
            'total_time': response.css('section > div:nth-child(1) > div:nth-child(3) > div.recipe-meta-item-body::text').get().strip(),
            'ingredients': response.css('.ingredients-item-name::text').getall(),
            'instruction': response.css('div.section-body > div > p::text').getall(),
            'rating': response.css('span.review-star-text::text')[0].get().strip(),
            'nutrition': response.css('section.nutrition-section.container > div > div.section-body::text').get().split(sep=';'),
            'Cuisine': 'Egyptian',
        }

    def parse(self, response):
        for recipe in response.css('div.component.card.card__category'):
            url = recipe.css("div.card__imageContainer a::attr(href)")[
                0].get().strip()
            next_page = response.urljoin(url)
            yield scrapy.Request(next_page, callback=self.parseRecipe)
        # for recipe in response.css('div.category-page-item > div.category-page-item-content'):
        #     url = recipe.css("a::attr(href)")[
        #         0].get().strip()
        #     next_page = response.urljoin(url)
        #     yield scrapy.Request(next_page, callback=self.parseRecipe)
