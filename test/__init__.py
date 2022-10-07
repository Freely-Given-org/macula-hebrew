import re
from lxml import etree

desired_filenames = [
    "01-Gen-001.xml",
    "01-Gen-002.xml",
    "01-Gen-003.xml",
    "01-Gen-004.xml",
    "01-Gen-005.xml",
    "01-Gen-006.xml",
    "01-Gen-007.xml",
    "01-Gen-008.xml",
    "01-Gen-009.xml",
    "01-Gen-010.xml",
    "01-Gen-011.xml",
    "01-Gen-012.xml",
    "01-Gen-013.xml",
    "01-Gen-014.xml",
    "01-Gen-015.xml",
    "01-Gen-016.xml",
    "01-Gen-017.xml",
    "01-Gen-018.xml",
    "01-Gen-019.xml",
    "01-Gen-020.xml",
    "01-Gen-021.xml",
    "01-Gen-022.xml",
    "01-Gen-023.xml",
    "01-Gen-024.xml",
    "01-Gen-025.xml",
    "01-Gen-026.xml",
    "01-Gen-027.xml",
    "01-Gen-028.xml",
    "01-Gen-029.xml",
    "01-Gen-030.xml",
    "01-Gen-031.xml",
    "01-Gen-032.xml",
    "01-Gen-033.xml",
    "01-Gen-034.xml",
    "01-Gen-035.xml",
    "01-Gen-036.xml",
    "01-Gen-037.xml",
    "01-Gen-038.xml",
    "01-Gen-039.xml",
    "01-Gen-040.xml",
    "01-Gen-041.xml",
    "01-Gen-042.xml",
    "01-Gen-043.xml",
    "01-Gen-044.xml",
    "01-Gen-045.xml",
    "01-Gen-046.xml",
    "01-Gen-047.xml",
    "01-Gen-048.xml",
    "01-Gen-049.xml",
    "01-Gen-050.xml",
    "02-Exo-001.xml",
    "02-Exo-002.xml",
    "02-Exo-003.xml",
    "02-Exo-004.xml",
    "02-Exo-005.xml",
    "02-Exo-006.xml",
    "02-Exo-007.xml",
    "02-Exo-008.xml",
    "02-Exo-009.xml",
    "02-Exo-010.xml",
    "02-Exo-011.xml",
    "02-Exo-012.xml",
    "02-Exo-013.xml",
    "02-Exo-014.xml",
    "02-Exo-015.xml",
    "02-Exo-016.xml",
    "02-Exo-017.xml",
    "02-Exo-018.xml",
    "02-Exo-019.xml",
    "02-Exo-020.xml",
    "02-Exo-021.xml",
    "02-Exo-022.xml",
    "02-Exo-023.xml",
    "02-Exo-024.xml",
    "02-Exo-025.xml",
    "02-Exo-026.xml",
    "02-Exo-027.xml",
    "02-Exo-028.xml",
    "02-Exo-029.xml",
    "02-Exo-030.xml",
    "02-Exo-031.xml",
    "02-Exo-032.xml",
    "02-Exo-033.xml",
    "02-Exo-034.xml",
    "02-Exo-035.xml",
    "02-Exo-036.xml",
    "02-Exo-037.xml",
    "02-Exo-038.xml",
    "02-Exo-039.xml",
    "02-Exo-040.xml",
    "03-Lev-001.xml",
    "03-Lev-002.xml",
    "03-Lev-003.xml",
    "03-Lev-004.xml",
    "03-Lev-005.xml",
    "03-Lev-006.xml",
    "03-Lev-007.xml",
    "03-Lev-008.xml",
    "03-Lev-009.xml",
    "03-Lev-010.xml",
    "03-Lev-011.xml",
    "03-Lev-012.xml",
    "03-Lev-013.xml",
    "03-Lev-014.xml",
    "03-Lev-015.xml",
    "03-Lev-016.xml",
    "03-Lev-017.xml",
    "03-Lev-018.xml",
    "03-Lev-019.xml",
    "03-Lev-020.xml",
    "03-Lev-021.xml",
    "03-Lev-022.xml",
    "03-Lev-023.xml",
    "03-Lev-024.xml",
    "03-Lev-025.xml",
    "03-Lev-026.xml",
    "03-Lev-027.xml",
    "04-Num-001.xml",
    "04-Num-002.xml",
    "04-Num-003.xml",
    "04-Num-004.xml",
    "04-Num-005.xml",
    "04-Num-006.xml",
    "04-Num-007.xml",
    "04-Num-008.xml",
    "04-Num-009.xml",
    "04-Num-010.xml",
    "04-Num-011.xml",
    "04-Num-012.xml",
    "04-Num-013.xml",
    "04-Num-014.xml",
    "04-Num-015.xml",
    "04-Num-016.xml",
    "04-Num-017.xml",
    "04-Num-018.xml",
    "04-Num-019.xml",
    "04-Num-020.xml",
    "04-Num-021.xml",
    "04-Num-022.xml",
    "04-Num-023.xml",
    "04-Num-024.xml",
    "04-Num-025.xml",
    "04-Num-026.xml",
    "04-Num-027.xml",
    "04-Num-028.xml",
    "04-Num-029.xml",
    "04-Num-030.xml",
    "04-Num-031.xml",
    "04-Num-032.xml",
    "04-Num-033.xml",
    "04-Num-034.xml",
    "04-Num-035.xml",
    "04-Num-036.xml",
    "05-Deu-001.xml",
    "05-Deu-002.xml",
    "05-Deu-003.xml",
    "05-Deu-004.xml",
    "05-Deu-005.xml",
    "05-Deu-006.xml",
    "05-Deu-007.xml",
    "05-Deu-008.xml",
    "05-Deu-009.xml",
    "05-Deu-010.xml",
    "05-Deu-011.xml",
    "05-Deu-012.xml",
    "05-Deu-013.xml",
    "05-Deu-014.xml",
    "05-Deu-015.xml",
    "05-Deu-016.xml",
    "05-Deu-017.xml",
    "05-Deu-018.xml",
    "05-Deu-019.xml",
    "05-Deu-020.xml",
    "05-Deu-021.xml",
    "05-Deu-022.xml",
    "05-Deu-023.xml",
    "05-Deu-024.xml",
    "05-Deu-025.xml",
    "05-Deu-026.xml",
    "05-Deu-027.xml",
    "05-Deu-028.xml",
    "05-Deu-029.xml",
    "05-Deu-030.xml",
    "05-Deu-031.xml",
    "05-Deu-032.xml",
    "05-Deu-033.xml",
    "05-Deu-034.xml",
    "06-Jos-001.xml",
    "06-Jos-002.xml",
    "06-Jos-003.xml",
    "06-Jos-004.xml",
    "06-Jos-005.xml",
    "06-Jos-006.xml",
    "06-Jos-007.xml",
    "06-Jos-008.xml",
    "06-Jos-009.xml",
    "06-Jos-010.xml",
    "06-Jos-011.xml",
    "06-Jos-012.xml",
    "06-Jos-013.xml",
    "06-Jos-014.xml",
    "06-Jos-015.xml",
    "06-Jos-016.xml",
    "06-Jos-017.xml",
    "06-Jos-018.xml",
    "06-Jos-019.xml",
    "06-Jos-020.xml",
    "06-Jos-021.xml",
    "06-Jos-022.xml",
    "06-Jos-023.xml",
    "06-Jos-024.xml",
    "07-Jdg-001.xml",
    "07-Jdg-002.xml",
    "07-Jdg-003.xml",
    "07-Jdg-004.xml",
    "07-Jdg-005.xml",
    "07-Jdg-006.xml",
    "07-Jdg-007.xml",
    "07-Jdg-008.xml",
    "07-Jdg-009.xml",
    "07-Jdg-010.xml",
    "07-Jdg-011.xml",
    "07-Jdg-012.xml",
    "07-Jdg-013.xml",
    "07-Jdg-014.xml",
    "07-Jdg-015.xml",
    "07-Jdg-016.xml",
    "07-Jdg-017.xml",
    "07-Jdg-018.xml",
    "07-Jdg-019.xml",
    "07-Jdg-020.xml",
    "07-Jdg-021.xml",
    "08-Rut-001.xml",
    "08-Rut-002.xml",
    "08-Rut-003.xml",
    "08-Rut-004.xml",
    "09-1Sa-001.xml",
    "09-1Sa-002.xml",
    "09-1Sa-003.xml",
    "09-1Sa-004.xml",
    "09-1Sa-005.xml",
    "09-1Sa-006.xml",
    "09-1Sa-007.xml",
    "09-1Sa-008.xml",
    "09-1Sa-009.xml",
    "09-1Sa-010.xml",
    "09-1Sa-011.xml",
    "09-1Sa-012.xml",
    "09-1Sa-013.xml",
    "09-1Sa-014.xml",
    "09-1Sa-015.xml",
    "09-1Sa-016.xml",
    "09-1Sa-017.xml",
    "09-1Sa-018.xml",
    "09-1Sa-019.xml",
    "09-1Sa-020.xml",
    "09-1Sa-021.xml",
    "09-1Sa-022.xml",
    "09-1Sa-023.xml",
    "09-1Sa-024.xml",
    "09-1Sa-025.xml",
    "09-1Sa-026.xml",
    "09-1Sa-027.xml",
    "09-1Sa-028.xml",
    "09-1Sa-029.xml",
    "09-1Sa-030.xml",
    "09-1Sa-031.xml",
    "10-2Sa-001.xml",
    "10-2Sa-002.xml",
    "10-2Sa-003.xml",
    "10-2Sa-004.xml",
    "10-2Sa-005.xml",
    "10-2Sa-006.xml",
    "10-2Sa-007.xml",
    "10-2Sa-008.xml",
    "10-2Sa-009.xml",
    "10-2Sa-010.xml",
    "10-2Sa-011.xml",
    "10-2Sa-012.xml",
    "10-2Sa-013.xml",
    "10-2Sa-014.xml",
    "10-2Sa-015.xml",
    "10-2Sa-016.xml",
    "10-2Sa-017.xml",
    "10-2Sa-018.xml",
    "10-2Sa-019.xml",
    "10-2Sa-020.xml",
    "10-2Sa-021.xml",
    "10-2Sa-022.xml",
    "10-2Sa-023.xml",
    "10-2Sa-024.xml",
    "11-1Ki-001.xml",
    "11-1Ki-002.xml",
    "11-1Ki-003.xml",
    "11-1Ki-004.xml",
    "11-1Ki-005.xml",
    "11-1Ki-006.xml",
    "11-1Ki-007.xml",
    "11-1Ki-008.xml",
    "11-1Ki-009.xml",
    "11-1Ki-010.xml",
    "11-1Ki-011.xml",
    "11-1Ki-012.xml",
    "11-1Ki-013.xml",
    "11-1Ki-014.xml",
    "11-1Ki-015.xml",
    "11-1Ki-016.xml",
    "11-1Ki-017.xml",
    "11-1Ki-018.xml",
    "11-1Ki-019.xml",
    "11-1Ki-020.xml",
    "11-1Ki-021.xml",
    "11-1Ki-022.xml",
    "12-2Ki-001.xml",
    "12-2Ki-002.xml",
    "12-2Ki-003.xml",
    "12-2Ki-004.xml",
    "12-2Ki-005.xml",
    "12-2Ki-006.xml",
    "12-2Ki-007.xml",
    "12-2Ki-008.xml",
    "12-2Ki-009.xml",
    "12-2Ki-010.xml",
    "12-2Ki-011.xml",
    "12-2Ki-012.xml",
    "12-2Ki-013.xml",
    "12-2Ki-014.xml",
    "12-2Ki-015.xml",
    "12-2Ki-016.xml",
    "12-2Ki-017.xml",
    "12-2Ki-018.xml",
    "12-2Ki-019.xml",
    "12-2Ki-020.xml",
    "12-2Ki-021.xml",
    "12-2Ki-022.xml",
    "12-2Ki-023.xml",
    "12-2Ki-024.xml",
    "12-2Ki-025.xml",
    "13-1Ch-001.xml",
    "13-1Ch-002.xml",
    "13-1Ch-003.xml",
    "13-1Ch-004.xml",
    "13-1Ch-005.xml",
    "13-1Ch-006.xml",
    "13-1Ch-007.xml",
    "13-1Ch-008.xml",
    "13-1Ch-009.xml",
    "13-1Ch-010.xml",
    "13-1Ch-011.xml",
    "13-1Ch-012.xml",
    "13-1Ch-013.xml",
    "13-1Ch-014.xml",
    "13-1Ch-015.xml",
    "13-1Ch-016.xml",
    "13-1Ch-017.xml",
    "13-1Ch-018.xml",
    "13-1Ch-019.xml",
    "13-1Ch-020.xml",
    "13-1Ch-021.xml",
    "13-1Ch-022.xml",
    "13-1Ch-023.xml",
    "13-1Ch-024.xml",
    "13-1Ch-025.xml",
    "13-1Ch-026.xml",
    "13-1Ch-027.xml",
    "13-1Ch-028.xml",
    "13-1Ch-029.xml",
    "14-2Ch-001.xml",
    "14-2Ch-002.xml",
    "14-2Ch-003.xml",
    "14-2Ch-004.xml",
    "14-2Ch-005.xml",
    "14-2Ch-006.xml",
    "14-2Ch-007.xml",
    "14-2Ch-008.xml",
    "14-2Ch-009.xml",
    "14-2Ch-010.xml",
    "14-2Ch-011.xml",
    "14-2Ch-012.xml",
    "14-2Ch-013.xml",
    "14-2Ch-014.xml",
    "14-2Ch-015.xml",
    "14-2Ch-016.xml",
    "14-2Ch-017.xml",
    "14-2Ch-018.xml",
    "14-2Ch-019.xml",
    "14-2Ch-020.xml",
    "14-2Ch-021.xml",
    "14-2Ch-022.xml",
    "14-2Ch-023.xml",
    "14-2Ch-024.xml",
    "14-2Ch-025.xml",
    "14-2Ch-026.xml",
    "14-2Ch-027.xml",
    "14-2Ch-028.xml",
    "14-2Ch-029.xml",
    "14-2Ch-030.xml",
    "14-2Ch-031.xml",
    "14-2Ch-032.xml",
    "14-2Ch-033.xml",
    "14-2Ch-034.xml",
    "14-2Ch-035.xml",
    "14-2Ch-036.xml",
    "15-Ezr-001.xml",
    "15-Ezr-002.xml",
    "15-Ezr-003.xml",
    "15-Ezr-004.xml",
    "15-Ezr-005.xml",
    "15-Ezr-006.xml",
    "15-Ezr-007.xml",
    "15-Ezr-008.xml",
    "15-Ezr-009.xml",
    "15-Ezr-010.xml",
    "16-Neh-001.xml",
    "16-Neh-002.xml",
    "16-Neh-003.xml",
    "16-Neh-004.xml",
    "16-Neh-005.xml",
    "16-Neh-006.xml",
    "16-Neh-007.xml",
    "16-Neh-008.xml",
    "16-Neh-009.xml",
    "16-Neh-010.xml",
    "16-Neh-011.xml",
    "16-Neh-012.xml",
    "16-Neh-013.xml",
    "17-Est-001.xml",
    "17-Est-002.xml",
    "17-Est-003.xml",
    "17-Est-004.xml",
    "17-Est-005.xml",
    "17-Est-006.xml",
    "17-Est-007.xml",
    "17-Est-008.xml",
    "17-Est-009.xml",
    "17-Est-010.xml",
    "18-Job-001.xml",
    "18-Job-002.xml",
    "18-Job-003.xml",
    "18-Job-004.xml",
    "18-Job-005.xml",
    "18-Job-006.xml",
    "18-Job-007.xml",
    "18-Job-008.xml",
    "18-Job-009.xml",
    "18-Job-010.xml",
    "18-Job-011.xml",
    "18-Job-012.xml",
    "18-Job-013.xml",
    "18-Job-014.xml",
    "18-Job-015.xml",
    "18-Job-016.xml",
    "18-Job-017.xml",
    "18-Job-018.xml",
    "18-Job-019.xml",
    "18-Job-020.xml",
    "18-Job-021.xml",
    "18-Job-022.xml",
    "18-Job-023.xml",
    "18-Job-024.xml",
    "18-Job-025.xml",
    "18-Job-026.xml",
    "18-Job-027.xml",
    "18-Job-028.xml",
    "18-Job-029.xml",
    "18-Job-030.xml",
    "18-Job-031.xml",
    "18-Job-032.xml",
    "18-Job-033.xml",
    "18-Job-034.xml",
    "18-Job-035.xml",
    "18-Job-036.xml",
    "18-Job-037.xml",
    "18-Job-038.xml",
    "18-Job-039.xml",
    "18-Job-040.xml",
    "18-Job-041.xml",
    "18-Job-042.xml",
    "19-Psa-001.xml",
    "19-Psa-002.xml",
    "19-Psa-003.xml",
    "19-Psa-004.xml",
    "19-Psa-005.xml",
    "19-Psa-006.xml",
    "19-Psa-007.xml",
    "19-Psa-008.xml",
    "19-Psa-009.xml",
    "19-Psa-010.xml",
    "19-Psa-011.xml",
    "19-Psa-012.xml",
    "19-Psa-013.xml",
    "19-Psa-014.xml",
    "19-Psa-015.xml",
    "19-Psa-016.xml",
    "19-Psa-017.xml",
    "19-Psa-018.xml",
    "19-Psa-019.xml",
    "19-Psa-020.xml",
    "19-Psa-021.xml",
    "19-Psa-022.xml",
    "19-Psa-023.xml",
    "19-Psa-024.xml",
    "19-Psa-025.xml",
    "19-Psa-026.xml",
    "19-Psa-027.xml",
    "19-Psa-028.xml",
    "19-Psa-029.xml",
    "19-Psa-030.xml",
    "19-Psa-031.xml",
    "19-Psa-032.xml",
    "19-Psa-033.xml",
    "19-Psa-034.xml",
    "19-Psa-035.xml",
    "19-Psa-036.xml",
    "19-Psa-037.xml",
    "19-Psa-038.xml",
    "19-Psa-039.xml",
    "19-Psa-040.xml",
    "19-Psa-041.xml",
    "19-Psa-042.xml",
    "19-Psa-043.xml",
    "19-Psa-044.xml",
    "19-Psa-045.xml",
    "19-Psa-046.xml",
    "19-Psa-047.xml",
    "19-Psa-048.xml",
    "19-Psa-049.xml",
    "19-Psa-050.xml",
    "19-Psa-051.xml",
    "19-Psa-052.xml",
    "19-Psa-053.xml",
    "19-Psa-054.xml",
    "19-Psa-055.xml",
    "19-Psa-056.xml",
    "19-Psa-057.xml",
    "19-Psa-058.xml",
    "19-Psa-059.xml",
    "19-Psa-060.xml",
    "19-Psa-061.xml",
    "19-Psa-062.xml",
    "19-Psa-063.xml",
    "19-Psa-064.xml",
    "19-Psa-065.xml",
    "19-Psa-066.xml",
    "19-Psa-067.xml",
    "19-Psa-068.xml",
    "19-Psa-069.xml",
    "19-Psa-070.xml",
    "19-Psa-071.xml",
    "19-Psa-072.xml",
    "19-Psa-073.xml",
    "19-Psa-074.xml",
    "19-Psa-075.xml",
    "19-Psa-076.xml",
    "19-Psa-077.xml",
    "19-Psa-078.xml",
    "19-Psa-079.xml",
    "19-Psa-080.xml",
    "19-Psa-081.xml",
    "19-Psa-082.xml",
    "19-Psa-083.xml",
    "19-Psa-084.xml",
    "19-Psa-085.xml",
    "19-Psa-086.xml",
    "19-Psa-087.xml",
    "19-Psa-088.xml",
    "19-Psa-089.xml",
    "19-Psa-090.xml",
    "19-Psa-091.xml",
    "19-Psa-092.xml",
    "19-Psa-093.xml",
    "19-Psa-094.xml",
    "19-Psa-095.xml",
    "19-Psa-096.xml",
    "19-Psa-097.xml",
    "19-Psa-098.xml",
    "19-Psa-099.xml",
    "19-Psa-100.xml",
    "19-Psa-101.xml",
    "19-Psa-102.xml",
    "19-Psa-103.xml",
    "19-Psa-104.xml",
    "19-Psa-105.xml",
    "19-Psa-106.xml",
    "19-Psa-107.xml",
    "19-Psa-108.xml",
    "19-Psa-109.xml",
    "19-Psa-110.xml",
    "19-Psa-111.xml",
    "19-Psa-112.xml",
    "19-Psa-113.xml",
    "19-Psa-114.xml",
    "19-Psa-115.xml",
    "19-Psa-116.xml",
    "19-Psa-117.xml",
    "19-Psa-118.xml",
    "19-Psa-119.xml",
    "19-Psa-120.xml",
    "19-Psa-121.xml",
    "19-Psa-122.xml",
    "19-Psa-123.xml",
    "19-Psa-124.xml",
    "19-Psa-125.xml",
    "19-Psa-126.xml",
    "19-Psa-127.xml",
    "19-Psa-128.xml",
    "19-Psa-129.xml",
    "19-Psa-130.xml",
    "19-Psa-131.xml",
    "19-Psa-132.xml",
    "19-Psa-133.xml",
    "19-Psa-134.xml",
    "19-Psa-135.xml",
    "19-Psa-136.xml",
    "19-Psa-137.xml",
    "19-Psa-138.xml",
    "19-Psa-139.xml",
    "19-Psa-140.xml",
    "19-Psa-141.xml",
    "19-Psa-142.xml",
    "19-Psa-143.xml",
    "19-Psa-144.xml",
    "19-Psa-145.xml",
    "19-Psa-146.xml",
    "19-Psa-147.xml",
    "19-Psa-148.xml",
    "19-Psa-149.xml",
    "19-Psa-150.xml",
    "20-Pro-001.xml",
    "20-Pro-002.xml",
    "20-Pro-003.xml",
    "20-Pro-004.xml",
    "20-Pro-005.xml",
    "20-Pro-006.xml",
    "20-Pro-007.xml",
    "20-Pro-008.xml",
    "20-Pro-009.xml",
    "20-Pro-010.xml",
    "20-Pro-011.xml",
    "20-Pro-012.xml",
    "20-Pro-013.xml",
    "20-Pro-014.xml",
    "20-Pro-015.xml",
    "20-Pro-016.xml",
    "20-Pro-017.xml",
    "20-Pro-018.xml",
    "20-Pro-019.xml",
    "20-Pro-020.xml",
    "20-Pro-021.xml",
    "20-Pro-022.xml",
    "20-Pro-023.xml",
    "20-Pro-024.xml",
    "20-Pro-025.xml",
    "20-Pro-026.xml",
    "20-Pro-027.xml",
    "20-Pro-028.xml",
    "20-Pro-029.xml",
    "20-Pro-030.xml",
    "20-Pro-031.xml",
    "21-Ecc-001.xml",
    "21-Ecc-002.xml",
    "21-Ecc-003.xml",
    "21-Ecc-004.xml",
    "21-Ecc-005.xml",
    "21-Ecc-006.xml",
    "21-Ecc-007.xml",
    "21-Ecc-008.xml",
    "21-Ecc-009.xml",
    "21-Ecc-010.xml",
    "21-Ecc-011.xml",
    "21-Ecc-012.xml",
    "22-Sng-001.xml",
    "22-Sng-002.xml",
    "22-Sng-003.xml",
    "22-Sng-004.xml",
    "22-Sng-005.xml",
    "22-Sng-006.xml",
    "22-Sng-007.xml",
    "22-Sng-008.xml",
    "23-Isa-001.xml",
    "23-Isa-002.xml",
    "23-Isa-003.xml",
    "23-Isa-004.xml",
    "23-Isa-005.xml",
    "23-Isa-006.xml",
    "23-Isa-007.xml",
    "23-Isa-008.xml",
    "23-Isa-009.xml",
    "23-Isa-010.xml",
    "23-Isa-011.xml",
    "23-Isa-012.xml",
    "23-Isa-013.xml",
    "23-Isa-014.xml",
    "23-Isa-015.xml",
    "23-Isa-016.xml",
    "23-Isa-017.xml",
    "23-Isa-018.xml",
    "23-Isa-019.xml",
    "23-Isa-020.xml",
    "23-Isa-021.xml",
    "23-Isa-022.xml",
    "23-Isa-023.xml",
    "23-Isa-024.xml",
    "23-Isa-025.xml",
    "23-Isa-026.xml",
    "23-Isa-027.xml",
    "23-Isa-028.xml",
    "23-Isa-029.xml",
    "23-Isa-030.xml",
    "23-Isa-031.xml",
    "23-Isa-032.xml",
    "23-Isa-033.xml",
    "23-Isa-034.xml",
    "23-Isa-035.xml",
    "23-Isa-036.xml",
    "23-Isa-037.xml",
    "23-Isa-038.xml",
    "23-Isa-039.xml",
    "23-Isa-040.xml",
    "23-Isa-041.xml",
    "23-Isa-042.xml",
    "23-Isa-043.xml",
    "23-Isa-044.xml",
    "23-Isa-045.xml",
    "23-Isa-046.xml",
    "23-Isa-047.xml",
    "23-Isa-048.xml",
    "23-Isa-049.xml",
    "23-Isa-050.xml",
    "23-Isa-051.xml",
    "23-Isa-052.xml",
    "23-Isa-053.xml",
    "23-Isa-054.xml",
    "23-Isa-055.xml",
    "23-Isa-056.xml",
    "23-Isa-057.xml",
    "23-Isa-058.xml",
    "23-Isa-059.xml",
    "23-Isa-060.xml",
    "23-Isa-061.xml",
    "23-Isa-062.xml",
    "23-Isa-063.xml",
    "23-Isa-064.xml",
    "23-Isa-065.xml",
    "23-Isa-066.xml",
    "24-Jer-001.xml",
    "24-Jer-002.xml",
    "24-Jer-003.xml",
    "24-Jer-004.xml",
    "24-Jer-005.xml",
    "24-Jer-006.xml",
    "24-Jer-007.xml",
    "24-Jer-008.xml",
    "24-Jer-009.xml",
    "24-Jer-010.xml",
    "24-Jer-011.xml",
    "24-Jer-012.xml",
    "24-Jer-013.xml",
    "24-Jer-014.xml",
    "24-Jer-015.xml",
    "24-Jer-016.xml",
    "24-Jer-017.xml",
    "24-Jer-018.xml",
    "24-Jer-019.xml",
    "24-Jer-020.xml",
    "24-Jer-021.xml",
    "24-Jer-022.xml",
    "24-Jer-023.xml",
    "24-Jer-024.xml",
    "24-Jer-025.xml",
    "24-Jer-026.xml",
    "24-Jer-027.xml",
    "24-Jer-028.xml",
    "24-Jer-029.xml",
    "24-Jer-030.xml",
    "24-Jer-031.xml",
    "24-Jer-032.xml",
    "24-Jer-033.xml",
    "24-Jer-034.xml",
    "24-Jer-035.xml",
    "24-Jer-036.xml",
    "24-Jer-037.xml",
    "24-Jer-038.xml",
    "24-Jer-039.xml",
    "24-Jer-040.xml",
    "24-Jer-041.xml",
    "24-Jer-042.xml",
    "24-Jer-043.xml",
    "24-Jer-044.xml",
    "24-Jer-045.xml",
    "24-Jer-046.xml",
    "24-Jer-047.xml",
    "24-Jer-048.xml",
    "24-Jer-049.xml",
    "24-Jer-050.xml",
    "24-Jer-051.xml",
    "24-Jer-052.xml",
    "25-Lam-001.xml",
    "25-Lam-002.xml",
    "25-Lam-003.xml",
    "25-Lam-004.xml",
    "25-Lam-005.xml",
    "26-Ezk-001.xml",
    "26-Ezk-002.xml",
    "26-Ezk-003.xml",
    "26-Ezk-004.xml",
    "26-Ezk-005.xml",
    "26-Ezk-006.xml",
    "26-Ezk-007.xml",
    "26-Ezk-008.xml",
    "26-Ezk-009.xml",
    "26-Ezk-010.xml",
    "26-Ezk-011.xml",
    "26-Ezk-012.xml",
    "26-Ezk-013.xml",
    "26-Ezk-014.xml",
    "26-Ezk-015.xml",
    "26-Ezk-016.xml",
    "26-Ezk-017.xml",
    "26-Ezk-018.xml",
    "26-Ezk-019.xml",
    "26-Ezk-020.xml",
    "26-Ezk-021.xml",
    "26-Ezk-022.xml",
    "26-Ezk-023.xml",
    "26-Ezk-024.xml",
    "26-Ezk-025.xml",
    "26-Ezk-026.xml",
    "26-Ezk-027.xml",
    "26-Ezk-028.xml",
    "26-Ezk-029.xml",
    "26-Ezk-030.xml",
    "26-Ezk-031.xml",
    "26-Ezk-032.xml",
    "26-Ezk-033.xml",
    "26-Ezk-034.xml",
    "26-Ezk-035.xml",
    "26-Ezk-036.xml",
    "26-Ezk-037.xml",
    "26-Ezk-038.xml",
    "26-Ezk-039.xml",
    "26-Ezk-040.xml",
    "26-Ezk-041.xml",
    "26-Ezk-042.xml",
    "26-Ezk-043.xml",
    "26-Ezk-044.xml",
    "26-Ezk-045.xml",
    "26-Ezk-046.xml",
    "26-Ezk-047.xml",
    "26-Ezk-048.xml",
    "27-Dan-001.xml",
    "27-Dan-002.xml",
    "27-Dan-003.xml",
    "27-Dan-004.xml",
    "27-Dan-005.xml",
    "27-Dan-006.xml",
    "27-Dan-007.xml",
    "27-Dan-008.xml",
    "27-Dan-009.xml",
    "27-Dan-010.xml",
    "27-Dan-011.xml",
    "27-Dan-012.xml",
    "28-HOS-001.xml",
    "28-HOS-002.xml",
    "28-HOS-003.xml",
    "28-HOS-004.xml",
    "28-HOS-005.xml",
    "28-HOS-006.xml",
    "28-HOS-007.xml",
    "28-HOS-008.xml",
    "28-HOS-009.xml",
    "28-HOS-010.xml",
    "28-HOS-011.xml",
    "28-HOS-012.xml",
    "28-HOS-013.xml",
    "28-HOS-014.xml",
    "29-Jol-001.xml",
    "29-Jol-002.xml",
    "29-Jol-003.xml",
    "29-Jol-004.xml",
    "30-Amo-001.xml",
    "30-Amo-002.xml",
    "30-Amo-003.xml",
    "30-Amo-004.xml",
    "30-Amo-005.xml",
    "30-Amo-006.xml",
    "30-Amo-007.xml",
    "30-Amo-008.xml",
    "30-Amo-009.xml",
    "31-Oba-001.xml",
    "32-Jon-001.xml",
    "32-Jon-002.xml",
    "32-Jon-003.xml",
    "32-Jon-004.xml",
    "33-Mic-001.xml",
    "33-Mic-002.xml",
    "33-Mic-003.xml",
    "33-Mic-004.xml",
    "33-Mic-005.xml",
    "33-Mic-006.xml",
    "33-Mic-007.xml",
    "34-Nam-001.xml",
    "34-Nam-002.xml",
    "34-Nam-003.xml",
    "35-Hab-001.xml",
    "35-Hab-002.xml",
    "35-Hab-003.xml",
    "36-Zep-001.xml",
    "36-Zep-002.xml",
    "36-Zep-003.xml",
    "37-Hag-001.xml",
    "37-Hag-002.xml",
    "38-Zec-001.xml",
    "38-Zec-002.xml",
    "38-Zec-003.xml",
    "38-Zec-004.xml",
    "38-Zec-005.xml",
    "38-Zec-006.xml",
    "38-Zec-007.xml",
    "38-Zec-008.xml",
    "38-Zec-009.xml",
    "38-Zec-010.xml",
    "38-Zec-011.xml",
    "38-Zec-012.xml",
    "38-Zec-013.xml",
    "38-Zec-014.xml",
    "39-Mal-001.xml",
    "39-Mal-002.xml",
    "39-Mal-003.xml",
]


def decorate_filename(filename, decorator):
    sub_regex = r"-" + decorator + r"\1"
    return re.sub(r"(.xml)", sub_regex, filename)


lowfat_path = "../lowfat/"
__lowfat_files__ = list(
    map(lambda x: lowfat_path + decorate_filename(x, "lowfat"), desired_filenames)
)

nodes_path = "../nodes/"
__nodes_files__ = list(map(lambda x: nodes_path + x, desired_filenames))

tei_path = "../Nestle1904/tei/"
__tei_files__ = list(map(lambda x: tei_path + x, desired_filenames))


def run_xpath_for_file(xpath, file):
    tree = etree.parse(file)
    return tree.xpath(xpath)
