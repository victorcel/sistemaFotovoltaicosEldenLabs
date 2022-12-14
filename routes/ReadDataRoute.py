import codecs
import csv
import uuid

from fastapi import APIRouter, UploadFile, Path, Depends

from models.ReadDataModel import ReadDataModel
from routes.LoginRoute import manager

router = APIRouter()

DB = {
    "readData": {}
}


@router.post("/send")
async def send_data(
        file: UploadFile,
        user=Depends(manager)
):
    csv_reader = csv.DictReader(codecs.iterdecode(file.file, "utf-8"))
    data_csv = []

    for rows in csv_reader:
        data_csv.append(ReadDataModel(
            id=str(uuid.uuid4()),
            connection_device_id=rows["ConnectionDeviceId"],
            hefesto_id=rows["HEFESTO_ID"],
            timestamp=rows["timestamp"],
            var_name=rows["var-name"],
            value=rows["value"],
            plugin=rows["plugin"],
            request=rows["request"],
            var_name_1=rows["var_name_1"],
            device=rows["device"],
        ))

    DB["readData"][file.filename] = {
        "data": data_csv
    }
    return DB["readData"]


@router.get("/load/{archive}")
async def get_data(
        archive: str = Path(...,
                            example="004f2464-67d5-44c1-aa12-428c504c5d49.csv"),
        user=Depends(manager)

):

    return DB["readData"].get(archive)
