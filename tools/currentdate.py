from typing import Optional
from crewai_tools import tool
from datetime import datetime


class GetCurrentDate:
    @tool("Get current date and time")
    def getRealtimeDate(_args: Optional[str] = "now"):
        """Useful for getting current and realtime date and time info. The paramater is the word now"""

        return datetime.now()


# t = GetCurrentDate()
# print(t.getRealtimeDate.run())
