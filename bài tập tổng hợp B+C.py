#bài tạp B0
def chuan_hoa_ten(ten):
    ten = ten.strip()          # bỏ khoảng trắng đầu và cuối
    ten = ' '.join(ten.split()) # bỏ khoảng trắng thừa giữa các từ
    ten = ten.title()          # viết hoa chữ cái đầu mỗi từ
    return ten

# Test
print(chuan_hoa_ten('  nguyễn   văn AN  '))

#bài tập B1
def phan_loai_huyet_ap(tam_thu, tam_truong):
    if tam_thu >= 140 or tam_truong >= 90:
        return 'Cao huyet ap'
    elif 120 <= tam_thu <= 139 or 80 <= tam_truong <= 89:
        return 'Tien cao huyet ap'
    else:
        return 'Binh thuong'

print(phan_loai_huyet_ap(130, 85))

#bài tập B2
def loc_huyet_ap(ds):
    ket_qua = []

    for bn in ds:
        if bn['huyet_ap'] >= 130:
            ket_qua.append(bn)

    return ket_qua

# Test
benh_nhan = [
    {'ten': 'An', 'tuoi': 20, 'huyet_ap': 135},
    {'ten': 'Binh', 'tuoi': 22, 'huyet_ap': 118},
    {'ten': 'Chi', 'tuoi': 19, 'huyet_ap': 142}
]

print(loc_huyet_ap(benh_nhan))

#bài tập B3
def tinh_bmi(can_nang, chieu_cao, don_vi_chieu_cao='m'):
    if don_vi_chieu_cao == 'cm':
        chieu_cao = chieu_cao / 100

    bmi = can_nang / (chieu_cao ** 2)

    if bmi < 18.5:
        phan_loai = 'Gay'
    elif bmi < 25:
        phan_loai = 'Binh thuong'
    elif bmi < 30:
        phan_loai = 'Thua can'
    else:
        phan_loai = 'Beo phi'

    return (round(bmi, 2), phan_loai)


print(tinh_bmi(65, 1.7))
print(tinh_bmi(65, 170, 'cm'))

#bài tập b4

def loc_va_ghi_file(file_vao: str, file_ra: str):
    with open(file_vao, mode="r", encoding="utf-8") as f_in:
        lines = f_in.readlines()
        
    if not lines:
        return

    ket_qua = [lines[0]] 

    for line in lines[1:]:
        line_clean = line.strip()
        if not line_clean:
            continue
        parts = line_clean.split(",")
        huyet_ap = int(parts[2])

        if huyet_ap > 130:
            ket_qua.append(line)

    with open(file_ra, mode="w", encoding="utf-8") as f_out:
        f_out.writelines(ket_qua)

# bài tập B5

def doc_tuoi_an_toan(gia_tri) -> int | None:
    try:
        return int(gia_tri)
    except ValueError:
        return None


# bài tập B6
class BenhNhan:
    def __init__(self, ten, tuoi, huyet_ap):
        self.ten = ten
        self.tuoi = tuoi
        self.huyet_ap = huyet_ap

    def canh_bao(self):
        if self.huyet_ap > 130:
            return True
        else:
            return False


print(BenhNhan("An", 20, 135).canh_bao())


#BÀI TẬP PHẦN C

class BenhNhan:
    def __init__(self, ten: str, tuoi: int, huyet_ap: int):
        self.ten = ten
        self.tuoi = tuoi
        self.huyet_ap = huyet_ap

    def canh_bao(self) -> bool:
        return self.huyet_ap > 130

    def lay_muc_do(self) -> str:
        if self.huyet_ap >= 140:
            return "Cao huyet ap"
        elif 120 <= self.huyet_ap <= 139:
            return "Tien cao huyet ap"
        else:
            return "Binh thuong"


def main():
    file_in = "benh_nhan.csv"
    file_out = "ket_qua_canh_bao.csv"

    # 1. Đọc file
    try:
        with open(file_in, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Không tìm thấy file {file_in}")
        return

    danh_sach_bn = []

    # 2. Xử lý dữ liệu từng dòng
    for line in lines[1:]:  # Bỏ tiêu đề
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        
        try:
            ten = parts[0].strip()
            tuoi = int(parts[1].strip())
            huyet_ap = int(parts[2].strip())
            danh_sach_bn.append(BenhNhan(ten, tuoi, huyet_ap))
        except ValueError:
            print(f"Cảnh báo: Dòng lỗi định dạng -> Bỏ qua: '{line}'")
            continue

    # 3. Lọc danh sách cảnh báo
    ds_canh_bao = [bn for bn in danh_sach_bn if bn.canh_bao()]

    # 4. In ra màn hình
    print("Danh sách cảnh báo:")
    for bn in ds_canh_bao:
        print(f"- {bn.ten}, {bn.tuoi} tuổi, Huyết áp: {bn.huyet_ap} ({bn.lay_muc_do()})")

    # 5. Ghi ra file CSV mới
    with open(file_out, "w", encoding="utf-8") as f:
        f.write("ten,tuoi,huyet_ap,muc_do\n")
        for bn in ds_canh_bao:
            f.write(f"{bn.ten},{bn.tuoi},{bn.huyet_ap},{bn.lay_muc_do()}\n")


if __name__ == "__main__":
    # Tạo file dữ liệu mẫu
    with open("benh_nhan.csv", "w", encoding="utf-8") as f:
        f.write("ten,tuoi,huyet_ap\nAn,20,135\nBinh,hai_muoi,118\nChi,19,142\n")
        
    main()
