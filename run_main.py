import sys
sys.path.append("F:\ly\API")
import pytest
if __name__=="__main__":
    pytest.main(['-s','--alluredir','./report/xml'])
# import pytest
# if __name__=="__main__":
#     pytest.main(['-s','-m=debug','--alluredir','./report/xml'])