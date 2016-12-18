# coding: utf-8
from __future__ import unicode_literals

from django.core.paginator import Paginator, Page


class FlynsarmyPaginator(Paginator):
    def __init__(self,
                 object_list,
                 per_page,
                 orphans=0,
                 allow_empty_first_page=True,
                 adjacent_pages=0):
        self.adjacent_pages = adjacent_pages
        super(FlynsarmyPaginator, self).__init__(object_list,
                                                 per_page,
                                                 orphans,
                                                 allow_empty_first_page)

    # Copied whole parent function returning a FlynsarmyPage instead. Ergh.
    # Better way of doing this?
    def page(self, number):
        "Returns a Page object for the given 1-based page number."
        number = self.validate_number(number)
        bottom = (number - 1) * self.per_page
        top = bottom + self.per_page
        if top + self.orphans >= self.count:
            top = self.count
        return FlynsarmyPage(self.object_list[bottom:top],
                             number,
                             self,
                             self.adjacent_pages)


class FlynsarmyPage(Page):
    def __init__(self, object_list, number, paginator, adjacent_pages=0):
        self.adjacent_pages = adjacent_pages
        super(FlynsarmyPage, self).__init__(object_list, number, paginator)

    def _get_page_range_data(self):
        """
        Returns a floating digg-style or 1-based  range of pages for
        iterating through within a template for loop.
        """
        if not self.adjacent_pages:
            return self.paginator.page_range

        startPage = max(1, self.number - self.adjacent_pages)
        # Be a bit smarter about start page
        if startPage <= 3:
            startPage = 1
        endPage = self.number + self.adjacent_pages + 1
        # Be a bit smarter about end page
        if endPage >= self.paginator.num_pages - 1:
            endPage = self.paginator.num_pages + 1

        page_range = [n for n in range(startPage, endPage)
                      if n > 0 and n <= self.paginator.count]

        return {
            'page_range': page_range,
            'show_first': 1 not in page_range,
            'show_last': self.paginator.num_pages not in page_range,
        }
    page_range_data = property(_get_page_range_data)
