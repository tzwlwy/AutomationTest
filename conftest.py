def pytest_configure(config):
   marker_list = ["abc","finished1","testmark3"]  # 标签名集合
   for markers in marker_list:
      config.addinivalue_line(
             "markers", markers
        )


   g=lambda a : a in marker_list
   lambda x: x ** 2
