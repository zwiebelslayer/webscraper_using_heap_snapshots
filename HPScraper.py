"""
As of now, this is the main Interface
"""
from playwright.sync_api import sync_playwright
from heap_snapshot_parser import ParserInterface


class HPScraper:
    def __init__(self, use_proxy=False, **kwargs):
        """
        :param user_agent: Optional: custom user agent if needed
        :param proxy: Optional: proxy if needed
        """
        self.use_proxy = use_proxy
        if use_proxy:
            self.proxy = kwargs.get('proxy')
        else:
            self.proxy = ""
        self.user_agent = kwargs.get('user_agent', '')
        self.heap_snapshot: str = ""
    
    def handle_sync_heapsnapshot(self, chunk: dict):
        """
        input: the event from the cdp session
        :return: nothing, will be used as a lambda
        """
        self.heap_snapshot += str(chunk["chunk"])
    
    def _sync_create_heap_snapshot(self, page_url: str, context_callback_function=None, page_callback_function=None):
        with sync_playwright() as p:
            if self.use_proxy:
                browser = p.chromium.launch(proxy=self.proxy)
            else:
                browser = p.chromium.launch()
            if len(self.user_agent) > 0:
                context = browser.new_context(user_agent=self.user_agent)
            else:
                context = browser.new_context()
            
            if context_callback_function is not None:
                context_callback_function(context)
            
            page = context.new_page()
            page.goto(page_url)
            
            if page_callback_function is not None:
                page_callback_function(page)
            
            client = page.context.new_cdp_session(page)  # open a cdp session
            # https://chromedevtools.github.io/devtools-protocol/v8/HeapProfiler/#method-takeHeapSnapshot
            client.on("HeapProfiler.addHeapSnapshotChunk", lambda event: self.handle_sync_heapsnapshot(event))
            create_snapshot = client.send(method='HeapProfiler.takeHeapSnapshot', params={"captureNumericValue": True})
    
    def query_page_for_props(self, page_url: str, query_strs: [str], context_callback_function=None,
                             page_callback_function=None, **kwargs) -> dict:
        """
        :param page_url: the url to scrape data from
        :param query_strs: For what properties will the page be queried
        :param callback_function: a function where the user can manipulate the page. the function receives the page from playwright
        :param kwargs:
        :return: the results
        
        This will create a heap snapshot and then query the page for properties
        """
        self.heap_snapshot = ""
        self._sync_create_heap_snapshot(page_url, context_callback_function, page_callback_function)
        if len(self.heap_snapshot) == 0:
            raise AssertionError("heap snapshot is empty")
        
        test_str = self.heap_snapshot
        
        parser = ParserInterface(test_str)
        parser.create_graph()
        query_result = parser.query(query_strs)
        parser.shutdown()
        return query_result
    
    async def async_query_page_for_props(self, page_urls: [str], query_strs: [str], callback_function=None,
                                         **kwargs) -> dict:
        """
        :param page_urls: list of urls to scrape data
        :param query_strs: For what properties will the page be queried
        :param callback_function: a function where the user can manipulate the page. the function receives the page from playwright
        :param kwargs:
        :return: the results
        """
        pass
