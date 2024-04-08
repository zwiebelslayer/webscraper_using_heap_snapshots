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
        
        if use_proxy:
            self.proxy = kwargs.get('proxy')
        else:
            self.proxy = ""
        self.user_agent = kwargs.get('proxy', '')
        self.heap_snapshot: str = ""
    
    def handle_sync_heapsnapshot(self, chunk: dict):
        """
        input: the event from the cdp session
        :return: nothing, will be used as a lambda
        """
        self.heap_snapshot += str(chunk["chunk"])
        
    def _sync_create_heap_snapshot(self, page_url: str):
        with sync_playwright() as p:
            if len(self.proxy) > 0:
                browser = p.chromium.launch()
            else:
                browser = p.chromium.launch()
            if len(self.user_agent) > 0:
                context = browser.new_context(user_agent=self.user_agent)
            else:
                context = browser.new_context()
            
            page = context.new_page()
            page.goto(page_url)
            client = page.context.new_cdp_session(page)  # open a cdp session
            """
            scroll with the mouse a bit to ensure that every data is loaded
            some pages only load the wanted information if you interact with it
            all values in this loop are random feel free to change them or remove the loop
            """
            #TODO: add some kind of hook to let the user click buttons on the page!
            for i in range(3):
                page.mouse.wheel(0, 15000)
            
            client.on("HeapProfiler.addHeapSnapshotChunk", lambda event: self.handle_sync_heapsnapshot(event))
            client.send('HeapProfiler.takeHeapSnapshot')
            
    
    def query_page_for_props(self, page_url: str, query_strs: [str], **kwargs) -> dict:
        """
        :param query_strs: For what properties will the page be queryied
        :param kwargs: proxy
        :return: the results
        
        This will create a heap snapshot and then query the page for properties
        """
        self.heap_snapshot = ""
        self._sync_create_heap_snapshot(page_url)
        if len(self.heap_snapshot) == 0:
            raise AssertionError("heap snapshot is empty")
        
        test_str = self.heap_snapshot
        
        with open("tesfile.json", "w") as f:
            f.write(test_str)
            
        parser = ParserInterface(test_str)
        parser.create_graph()
        query_result = parser.query(query_strs)
        parser.shutdown()
        return query_result
