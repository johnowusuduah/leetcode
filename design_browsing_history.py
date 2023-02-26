#You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in 
#the history number of steps.

#Implement the BrowserHistory class:

#BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
#void visit(string url) Visits url from the current page. It clears up all the forward history.
#string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current 
#url after moving back in history at most steps.
#string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return 
#the current url after forwarding in history at most steps.

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current_page = homepage
        self.steptrack = 0
        self.history = [homepage]
    
    def visit(self, url: str) -> None:
        # TRICKY PART
        # keep popping until the last page in history is the current current_page
        # link between initialized self.steptrack at 0 and len(self.history) - 1
        while len(self.history)-1 > self.steptrack:
            self.history.pop()
        self.history.append(url)
        self.steptrack += 1

    def back(self, steps: int) -> str:
        if steps > self.steptrack:
            self.steptrack = 0
            self.current_page = self.history[self.steptrack]
            return self.current_page
        else:
            self.steptrack -= steps
            self.current_page = self.history[self.steptrack]
            return self.current_page
        
    def forward(self, steps: int) -> str:
        last_index = len(self.history)-1
        if self.steptrack + steps > last_index:
            self.steptrack = last_index
            self.current_page = self.history[self.steptrack]
            return self.current_page
        else:
            self.steptrack += steps
            self.current_page = self.history[self.steptrack]
            return self.current_page


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)