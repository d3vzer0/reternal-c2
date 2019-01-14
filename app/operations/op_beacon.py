from app.models import Beacons, BeaconHistory, TaskResults, Tasks
import mongoengine


class Beacon:
    def __init__(self, beacon_id):
        self.beacon_id = beacon_id

    def get(self):
        try:
            beacon_object = Beacons.objects.get(beacon_id=self.beacon_id)
            result = {"result":"success", "data":"Beacon exists"}

        except mongoengine.errors.DoesNotExist:
            result = {"result":"failed", "data":"Beacon does not exist"}

        except Exception as err:
            result = {"result":"failed", "data":"Unable to query beacon"}

        return result


    def create(self, beacon_os, username, timer, hostname, beacon_data, working_dir, remote_ip=""):
        try:
            beacon_object = Beacons(
                beacon_id=self.beacon_id, platform=beacon_os,
                data=beacon_data, hostname=hostname, username=username,
                working_dir=working_dir, remote_ip=remote_ip
            ).save()

            result = {"result": "success", "data": "Beacon succesfully added"}

        except mongoengine.errors.NotUniqueError:
            result = {"result": "failed", "message": "Beacon already exists"}

        except Exception as err:
            result = {"result": "failed", "data": "Unable to add beacon to database"}

        return result

 