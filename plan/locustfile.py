import random
from locust import HttpUser, constant, task, between,constant_throughput
max_devices = 6
playback_auth_domain = 'cheetahmen.chocotv.com.tw'
instance_num = random.randint(1, max_devices)
query_str = r'appId=062097f1b1f34e11e7f82aag22000aee&' + r'chocomemberAppId=86a6b258-ac30-4816-bc14-a31e514226d7&countryCode=TW&languageId=zh'
headers = {
    'Authorization': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50SWQiOiI3YzEwYmQ4My1hYTUzLTQ2Y2YtYWI1Zi05MDViY2NiMzZmZjQiLCJhcHBJZCI6Ijg2YTZiMjU4LWFjMzAtNDgxNi1iYzE0LWEzMWU1MTQyMjZkNyIsImxpY2VuY2UiOiJ1c2VyIiwic2NvcGUiOiJyZWFkIiwiaWF0IjoxNjQ4MDA2ODA4LCJleHAiOjE2NDg2MTE2MDh9.TNDtNZV3GaFm-WVRS1xAAVKwkGPm8R6ebIawM6pPcZpAMETKbiopT6Ar4ALKNV1ODckjysuKRv2Ku7k9XZHBE9Avkr7p20O46_94VJIAzzggu0RTLgEWKOpmzujE5GB0oIBO_ND0EXQSgGxkmTmaMDnBMi4GkcBI3-NAWE0L7kc',
    'Content-Type': 'application/json'
}
body = {
    'instanceId': str(instance_num),
    'deviceName': 'Firefox',
    'dramaName': 'testDrama',
    'dramaId': 'testId'
}
class LocustTest(HttpUser):
    wait_time = between(0.5, 2)

    @task
    def test(self):
        self.client.post(f"/v1/playbackAuth?{query_str}", headers=headers, json=body)