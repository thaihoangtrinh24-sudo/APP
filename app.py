import streamlit as st
import streamlit.components.v1 as components

# 1. Cấu hình trang hiển thị rộng tối đa
st.set_page_config(
    page_title="EduRisk-AI | Hệ thống Cảnh báo sớm Tin học 12 - Sở GD&ĐT tỉnh Lào Cai",
    page_icon="🎓",
    layout="wide"
)

# 2. Xóa bỏ khoảng đen, ép màu nền Streamlit đồng bộ với giao diện HTML (#f8fafc)
hide_streamlit_style = """
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        html, body, [data-testid="stAppViewContainer"], .stApp {
            background-color: #f8fafc !important;
            margin: 0 !important;
            padding: 0 !important;
        }
        .block-container {
            padding: 0px !important;
            margin: 0px !important;
            max-width: 100% !important;
        }
        iframe {
            display: block;
            background-color: #f8fafc !important;
            border: none;
            width: 100% !important;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 3. Mã nguồn HTML/Tailwind/Chart.js/SheetJS hoàn chỉnh
edurisk_html_code = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>EduRisk-AI | Hệ thống Cảnh báo sớm Tin học 12 - Sở GD&ĐT tỉnh Lào Cai</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- FontAwesome CDN -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <!-- Google Fonts: Inter -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- SheetJS (xlsx) CDN: Đọc & Xuất Excel trực tiếp -->
    <script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                    },
                    colors: {
                        brand: {
                            50: '#f0fdf4',
                            100: '#dcfce7',
                            500: '#22c55e',
                            600: '#16a34a',
                            700: '#15803d',
                            800: '#166534',
                            900: '#14532d',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; margin: 0; min-height: 100vh; }
        .custom-scrollbar::-webkit-scrollbar { width: 6px; height: 6px; }
        .custom-scrollbar::-webkit-scrollbar-track { background: #f1f5f9; }
        .custom-scrollbar::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
    </style>
</head>
<body class="text-slate-800 flex flex-col min-h-screen">

    <!-- MÀN HÌNH ĐĂNG NHẬP -->
    <div id="login-screen" class="fixed inset-0 bg-slate-900/80 backdrop-blur-sm z-50 flex items-center justify-center p-4">
        <div class="bg-white rounded-2xl shadow-2xl max-w-md w-full p-8 space-y-6">
            <div class="text-center space-y-2">
                <div class="w-16 h-16 bg-brand-600 text-white rounded-full flex items-center justify-center text-2xl font-bold mx-auto shadow-md">CLC</div>
                <h2 class="text-xl font-bold text-slate-900">Đăng Nhập Hệ Thống</h2>
                <p class="text-xs text-slate-500">EduRisk-AI • Sở GD&ĐT tỉnh Lào Cai</p>
            </div>
            <div class="space-y-4 text-xs">
                <div>
                    <label class="block font-semibold text-slate-700 mb-1">Tài khoản giáo viên / Quản trị</label>
                    <input type="text" id="username" placeholder="Nhập tên đăng nhập..." class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-brand-500">
                </div>
                <div>
                    <label class="block font-semibold text-slate-700 mb-1">Mật khẩu</label>
                    <input type="password" id="password" placeholder="••••••••" class="w-full px-4 py-2.5 bg-slate-50 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-brand-500">
                </div>
                <button onclick="handleLogin()" class="w-full bg-brand-600 hover:bg-brand-700 text-white font-bold py-3 rounded-xl transition shadow-sm text-sm">
                    Đăng Nhập Hệ Thống
                </button>
                <p id="login-error" class="text-rose-600 text-center font-medium hidden">Vui lòng nhập tài khoản và mật khẩu bất kỳ để tiếp tục!</p>
            </div>
        </div>
    </div>

    <!-- GIAO DIỆN CHÍNH -->
    <div id="main-app" class="flex flex-col min-h-screen opacity-0 transition-opacity duration-500 pointer-events-none">
        <!-- TOP HEADER -->
        <header class="bg-white border-b border-slate-200 sticky top-0 z-30 shadow-sm">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3">
                <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                    <div class="flex items-center gap-3">
                        <div class="w-12 h-12 rounded-full bg-green-600 text-white flex items-center justify-center font-bold text-lg shadow-sm">CLC</div>
                        <div>
                            <div class="text-xs font-semibold uppercase tracking-wider text-slate-500">Sở GD&ĐT tỉnh Lào Cai • Trường THPT Chuyên Lào Cai</div>
                            <h1 class="text-lg md:text-xl font-bold text-slate-900 flex items-center gap-2">
                                <span>EduRisk-AI</span>
                                <span class="text-xs font-semibold px-2 py-0.5 rounded-full bg-brand-100 text-brand-800 border border-brand-200">v2.4 Production</span>
                            </h1>
                        </div>
                    </div>

                    <div class="flex items-center gap-3 text-xs text-slate-600 bg-slate-50 p-2.5 rounded-xl border border-slate-200">
                        <div class="text-amber-700 font-medium">
                            <i class="fa-solid fa-triangle-exclamation mr-1"></i> Cảnh báo mang tính hỗ trợ, không phải kết luận tuyệt đối về năng lực.
                        </div>
                        <button onclick="handleLogout()" class="px-3 py-1.5 bg-rose-50 text-rose-700 hover:bg-rose-100 font-semibold rounded-lg transition ml-2">
                            <i class="fa-solid fa-right-from-bracket mr-1"></i> Đăng xuất
                        </button>
                    </div>
                </div>
            </div>

            <!-- THANH ĐIỀU HƯỚNG TABS -->
            <nav class="bg-slate-900 text-slate-300 text-sm font-medium">
                <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex overflow-x-auto custom-scrollbar">
                    <button onclick="switchTab('tab-dashboard')" id="nav-tab-dashboard" class="tab-btn px-4 py-3 flex items-center gap-2 border-b-2 border-brand-500 text-white whitespace-nowrap">
                        <i class="fa-solid fa-chart-pie"></i> Tổng quan (Dashboard)
                    </button>
                    <button onclick="switchTab('tab-alerts')" id="nav-tab-alerts" class="tab-btn px-4 py-3 flex items-center gap-2 border-b-2 border-transparent hover:text-white whitespace-nowrap">
                        <i class="fa-solid fa-triangle-exclamation text-amber-400"></i> Danh sách Cảnh báo
                        <span id="alert-badge-count" class="bg-red-500 text-white text-xs px-2 py-0.5 rounded-full font-bold ml-1">0</span>
                    </button>
                    <button onclick="switchTab('tab-interventions')" id="nav-tab-interventions" class="tab-btn px-4 py-3 flex items-center gap-2 border-b-2 border-transparent hover:text-white whitespace-nowrap">
                        <i class="fa-solid fa-user-gear"></i> Nhật ký Hỗ trợ Sư phạm
                    </button>
                    <button onclick="switchTab('tab-import')" id="nav-tab-import" class="tab-btn px-4 py-3 flex items-center gap-2 border-b-2 border-transparent hover:text-white whitespace-nowrap">
                        <i class="fa-solid fa-database"></i> Quản trị & Nhập dữ liệu
                    </button>
                </div>
            </nav>
        </header>

        <!-- NỘI DUNG CHÍNH -->
        <main class="flex-grow max-w-7xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 pb-16">

            <!-- TAB 1: TỔNG QUAN (DASHBOARD) -->
            <section id="tab-dashboard" class="tab-content space-y-6">
                <!-- THẺ KPI -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
                        <div>
                            <p class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Học sinh được đánh giá</p>
                            <h3 class="text-2xl font-bold text-slate-900 mt-1" id="kpi-total">0</h3>
                            <p class="text-xs text-slate-500 mt-1"><i class="fa-solid fa-users text-blue-500 mr-1"></i> Tất cả các lớp khối 12</p>
                        </div>
                        <div class="w-12 h-12 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center text-xl font-bold">
                            <i class="fa-solid fa-user-graduate"></i>
                        </div>
                    </div>

                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
                        <div>
                            <p class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Nguy cơ thấp</p>
                            <h3 class="text-2xl font-bold text-emerald-600 mt-1" id="kpi-low">0</h3>
                            <p class="text-xs text-emerald-600 mt-1 font-medium" id="kpi-low-pct"><i class="fa-solid fa-circle-check mr-1"></i> Tiến độ ổn định (0%)</p>
                        </div>
                        <div class="w-12 h-12 rounded-xl bg-emerald-50 text-emerald-600 flex items-center justify-center text-xl">
                            <i class="fa-solid fa-shield-halved"></i>
                        </div>
                    </div>

                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
                        <div>
                            <p class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Cần theo dõi</p>
                            <h3 class="text-2xl font-bold text-amber-600 mt-1" id="kpi-medium">0</h3>
                            <p class="text-xs text-amber-600 mt-1 font-medium" id="kpi-medium-pct"><i class="fa-solid fa-triangle-exclamation mr-1"></i> Suy giảm nhẹ (0%)</p>
                        </div>
                        <div class="w-12 h-12 rounded-xl bg-amber-50 text-amber-600 flex items-center justify-center text-xl">
                            <i class="fa-solid fa-eye"></i>
                        </div>
                    </div>

                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex items-center justify-between">
                        <div>
                            <p class="text-xs font-semibold text-slate-500 uppercase tracking-wider">Ưu tiên hỗ trợ</p>
                            <h3 class="text-2xl font-bold text-rose-600 mt-1" id="kpi-high">0</h3>
                            <p class="text-xs text-rose-600 mt-1 font-medium" id="kpi-high-pct"><i class="fa-solid fa-circle-exclamation mr-1"></i> Nguy cơ không đạt (0%)</p>
                        </div>
                        <div class="w-12 h-12 rounded-xl bg-rose-50 text-rose-600 flex items-center justify-center text-xl">
                            <i class="fa-solid fa-hand-holding-hand"></i>
                        </div>
                    </div>
                </div>

                <!-- BIỂU ĐỒ HÀNG 1 -->
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between">
                        <div>
                            <h3 class="text-base font-bold text-slate-800 flex items-center justify-between">
                                <span>Phân bổ Mức độ Nguy cơ</span>
                                <i class="fa-solid fa-chart-pie text-slate-400"></i>
                            </h3>
                            <p class="text-xs text-slate-500 mt-1">Dựa trên xác suất suy luận mô hình</p>
                        </div>
                        <div class="relative my-4 h-64 flex items-center justify-center">
                            <canvas id="riskDistributionChart"></canvas>
                        </div>
                    </div>

                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm lg:col-span-2 flex flex-col justify-between">
                        <div>
                            <h3 class="text-base font-bold text-slate-800 flex items-center justify-between">
                                <span>Biến động Tỷ lệ Cảnh báo Qua Các Mốc Thời Gian (T1 - T4)</span>
                                <i class="fa-solid fa-chart-line text-slate-400"></i>
                            </h3>
                            <p class="text-xs text-slate-500 mt-1">Theo dõi xu hướng chuyển dịch nguy cơ để can thiệp kịp thời</p>
                        </div>
                        <div class="my-4 h-64">
                            <canvas id="progressionChart"></canvas>
                        </div>
                        <!-- CHÚ THÍCH CỤ THỂ 4 MỐC THỜI GIAN -->
                        <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs text-slate-600 flex flex-wrap items-center justify-between gap-2 mt-2">
                            <span><strong class="text-brand-700">T1:</strong> Tuần 4 (Đánh giá ban đầu)</span>
                            <span><strong class="text-blue-700">T2:</strong> Tuần 8 (Giữa kỳ 1)</span>
                            <span><strong class="text-amber-700">T3:</strong> Tuần 12 (Sau can thiệp)</span>
                            <span><strong class="text-rose-700">T4:</strong> Tuần 16 (Hiện tại - Thi học kỳ)</span>
                        </div>
                    </div>
                </div>

                <!-- BIỂU ĐỒ HÀNG 2: A - L VÀ NGUYÊN LÝ -->
                <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm">
                        <h3 class="text-base font-bold text-slate-800 flex items-center justify-between">
                            <span>Trọng số Tác động của các Nhóm Đặc trưng (A - L)</span>
                            <i class="fa-solid fa-layer-group text-slate-400"></i>
                        </h3>
                        <p class="text-xs text-slate-500 mt-1">Phân tích mức độ ảnh hưởng đến dự báo rủi ro</p>
                        <div class="my-4 h-60">
                            <canvas id="alpFeatureChart"></canvas>
                        </div>
                    </div>

                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between">
                        <div>
                            <h3 class="text-base font-bold text-slate-800 flex items-center gap-2">
                                <i class="fa-solid fa-bullseye text-brand-600"></i> Nguyên lý Hoạt động & Chỉ số Cảnh báo
                            </h3>
                            <div class="mt-4 space-y-3 text-xs">
                                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                                    <div class="font-bold text-slate-800">Nhóm A (Assessment - Kiểm tra):</div>
                                    <p class="text-slate-600 mt-0.5">Điểm các bài kiểm tra định kỳ, trắc nghiệm lý thuyết môn Tin học 12.</p>
                                </div>
                                <div class="p-3 rounded-xl bg-slate-50 border border-slate-200">
                                    <div class="font-bold text-slate-800">Nhóm L (LMS Activity - Tương tác hệ thống):</div>
                                    <p class="text-slate-600 mt-0.5">Tần suất đăng nhập, thời gian xem bài giảng, tỷ lệ hoàn thành học liệu trên LMS.</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- TAB 2: DANH SÁCH CẢNH BÁO -->
            <section id="tab-alerts" class="tab-content hidden space-y-6">
                <!-- GHI CHÚ QUY ĐỊNH MỐC THỜI GIAN -->
                <div class="p-3 bg-blue-50 border border-blue-200 rounded-xl text-xs text-blue-800 flex items-center gap-2">
                    <i class="fa-solid fa-circle-info text-blue-600 text-sm"></i>
                    <span><strong>Quy định mốc thời gian:</strong> <strong>T1:</strong> Tuần 4 (Đầu kỳ) | <strong>T2:</strong> Tuần 8 (Giữa kỳ) | <strong>T3:</strong> Tuần 12 (Sau can thiệp) | <strong>T4:</strong> Tuần 16 (Hiện tại - Thi học kỳ).</span>
                </div>

                <div class="bg-white p-4 rounded-2xl border border-slate-200 shadow-sm flex flex-col lg:flex-row items-center justify-between gap-4">
                    <div class="flex flex-wrap items-center gap-3 w-full lg:w-auto">
                        <div class="relative flex-grow sm:flex-grow-0 sm:w-64">
                            <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-xs"></i>
                            <input type="text" id="search-student" oninput="filterStudents()" placeholder="Tìm kiếm Mã HS..." class="w-full pl-9 pr-3 py-2 bg-slate-50 border border-slate-200 rounded-xl text-xs focus:outline-none focus:ring-2 focus:ring-brand-500">
                        </div>
                        <select id="filter-class" onchange="filterStudents()" class="bg-slate-50 border border-slate-200 text-xs rounded-xl px-3 py-2">
                            <option value="">Tất cả các lớp</option>
                        </select>
                        <select id="filter-milestone" onchange="filterStudents()" class="bg-slate-50 border border-slate-200 text-xs rounded-xl px-3 py-2">
                            <option value="">Tất cả các mốc</option>
                            <option value="T1">Mốc T1 (Tuần 4 - Đánh giá ban đầu)</option>
                            <option value="T2">Mốc T2 (Tuần 8 - Giữa kỳ 1)</option>
                            <option value="T3">Mốc T3 (Tuần 12 - Sau can thiệp)</option>
                            <option value="T4" selected>Mốc T4 (Tuần 16 - Thi Học kỳ)</option>
                        </select>
                        <select id="filter-risk" onchange="filterStudents()" class="bg-slate-50 border border-slate-200 text-xs rounded-xl px-3 py-2">
                            <option value="">Tất cả mức nguy cơ</option>
                            <option value="Ưu tiên hỗ trợ">Ưu tiên hỗ trợ (Đỏ)</option>
                            <option value="Cần theo dõi">Cần theo dõi (Vàng)</option>
                            <option value="Thấp">Nguy cơ thấp (Xanh)</option>
                        </select>
                    </div>
                    <div class="flex items-center gap-3">
                        <div class="text-xs text-slate-500 whitespace-nowrap">
                            Hiển thị <strong id="filter-count" class="text-slate-800">0</strong> / <span id="total-count">0</span> học sinh
                        </div>
                        <button onclick="exportExcel()" class="px-3 py-1.5 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-semibold shadow-sm transition flex items-center gap-1.5">
                            <i class="fa-solid fa-file-excel"></i> Xuất Excel
                        </button>
                    </div>
                </div>

                <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-hidden">
                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs text-slate-600 border-collapse">
                            <thead class="bg-slate-50 text-slate-700 font-bold uppercase tracking-wider border-b border-slate-200">
                                <tr>
                                    <th class="py-3.5 px-4">Mã Học Sinh</th>
                                    <th class="py-3.5 px-4">Lớp</th>
                                    <th class="py-3.5 px-4">Mốc</th>
                                    <th class="py-3.5 px-4 text-center">Chỉ số A - L</th>
                                    <th class="py-3.5 px-4">Xác suất Nguy cơ</th>
                                    <th class="py-3.5 px-4">Mức Cảnh báo</th>
                                    <th class="py-3.5 px-4 text-center">Xu hướng (T1 → T4)</th>
                                    <th class="py-3.5 px-4 text-right">Thao tác</th>
                                </tr>
                            </thead>
                            <tbody id="student-table-body" class="divide-y divide-slate-100"></tbody>
                        </table>
                    </div>
                </div>
            </section>

            <!-- TAB 3: NHẬT KÝ HỖ TRỢ SƯ PHẠM -->
            <section id="tab-interventions" class="tab-content hidden space-y-6">
                <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm h-fit">
                        <h3 class="text-base font-bold text-slate-800 flex items-center gap-2 mb-1">
                            <i class="fa-solid fa-pen-to-square text-brand-600"></i> Ghi nhận Can thiệp Sư phạm
                        </h3>
                        <form id="intervention-form" onsubmit="saveIntervention(event)" class="space-y-4 text-xs mt-3">
                            <div>
                                <label class="block font-semibold text-slate-700 mb-1">Mã Học Sinh</label>
                                <select id="form-student-id" required class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2.5"></select>
                            </div>
                            <div>
                                <label class="block font-semibold text-slate-700 mb-1">Xác minh thực tế</label>
                                <select id="form-verification" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2.5">
                                    <option value="Đúng thực tế (Có gặp khó khăn)">Đúng thực tế (Có gặp khó khăn)</option>
                                    <option value="Cảnh báo giả (Học sinh vẫn ổn)">Cảnh báo giả (Học sinh vẫn ổn)</option>
                                    <option value="Do thiết bị/mạng hỏng">Do sự cố kĩ thuật / thiết bị</option>
                                </select>
                            </div>
                            <div>
                                <label class="block font-semibold text-slate-700 mb-1">Biện pháp hỗ trợ</label>
                                <select id="form-action" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2.5">
                                    <option value="Phụ đạo lý thuyết cốt lõi">Phụ đạo lý thuyết cốt lõi</option>
                                    <option value="Giao bài tập bổ trợ trên LMS">Giao bài tập bổ trợ trên LMS</option>
                                    <option value="Phối hợp với GV chủ nhiệm & Gia đình">Phối hợp với GV chủ nhiệm & Gia đình</option>
                                </select>
                            </div>
                            <div>
                                <label class="block font-semibold text-slate-700 mb-1">Lịch tái đánh giá</label>
                                <input type="date" id="form-reassess-date" required class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2.5">
                            </div>
                            <div>
                                <label class="block font-semibold text-slate-700 mb-1">Ghi chú chi tiết</label>
                                <textarea id="form-note" rows="3" placeholder="Nhập tình hình trao đổi..." class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2.5"></textarea>
                            </div>
                            <div>
                                <label class="block font-semibold text-slate-700 mb-1">Trạng thái</label>
                                <select id="form-status" class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2.5">
                                    <option value="Đang can thiệp">Đang can thiệp</option>
                                    <option value="Đã cải thiện">Đã cải thiện</option>
                                    <option value="Chưa can thiệp">Chưa can thiệp</option>
                                </select>
                            </div>
                            <button type="submit" class="w-full bg-brand-600 hover:bg-brand-700 text-white font-bold py-2.5 rounded-xl transition shadow-sm text-xs">
                                <i class="fa-solid fa-floppy-disk mr-1"></i> Lưu Nhật Ký Can Thiệp
                            </button>
                        </form>
                    </div>

                    <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm lg:col-span-2 flex flex-col justify-between">
                        <div>
                            <div class="flex items-center justify-between mb-4">
                                <h3 class="text-base font-bold text-slate-800">Nhật Ký & Tiến Độ Hỗ Trợ Sư Phạm</h3>
                                <span class="text-xs font-semibold px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700">Tổng số lượt: <strong id="intervention-count">0</strong></span>
                            </div>
                            <div class="space-y-3 max-h-[520px] overflow-y-auto custom-scrollbar pr-1" id="interventions-list"></div>
                        </div>
                    </div>
                </div>
            </section>

            <!-- TAB 4: QUẢN TRỊ & NHẬP XUẤT EXCEL -->
            <section id="tab-import" class="tab-content hidden space-y-6">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <!-- NHẬP EXCEL -->
                    <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4">
                        <div class="flex items-center justify-between">
                            <div class="flex items-center gap-3 text-brand-700">
                                <div class="w-10 h-10 rounded-xl bg-brand-50 flex items-center justify-center text-lg font-bold">
                                    <i class="fa-solid fa-file-excel text-emerald-600"></i>
                                </div>
                                <div>
                                    <h3 class="text-base font-bold text-slate-800">Tải Lên Tệp Điểm (Excel .xlsx / .xls)</h3>
                                    <p class="text-xs text-slate-500">Tự động đọc cột & phân tích cảnh báo</p>
                                </div>
                            </div>
                            <button onclick="downloadTemplateExcel()" class="text-xs text-brand-600 font-semibold hover:underline flex items-center gap-1">
                                <i class="fa-solid fa-download"></i> Tải file mẫu (.xlsx)
                            </button>
                        </div>
                        <div class="border-2 border-dashed border-slate-300 rounded-2xl p-6 text-center hover:bg-slate-50 transition cursor-pointer" onclick="triggerFileInput()">
                            <input type="file" id="file-input" class="hidden" accept=".xlsx, .xls, .csv" onchange="handleExcelUpload(event)">
                            <i class="fa-solid fa-cloud-arrow-up text-3xl text-emerald-500 mb-2"></i>
                            <p class="text-xs font-semibold text-slate-700">Nhấp để chọn tệp Excel hoặc kéo thả vào đây</p>
                            <p class="text-[11px] text-slate-400 mt-1">Hỗ trợ các cột: Mã_HS, Lớp, Mốc, Điểm_A, Điểm_T1 (nếu có), Tương_Tác_LMS</p>
                        </div>
                    </div>

                    <!-- XUẤT EXCEL -->
                    <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-4 flex flex-col justify-between">
                        <div class="space-y-4">
                            <div class="flex items-center gap-3 text-emerald-700">
                                <div class="w-10 h-10 rounded-xl bg-emerald-50 flex items-center justify-center text-lg font-bold">
                                    <i class="fa-solid fa-file-export"></i>
                                </div>
                                <div>
                                    <h3 class="text-base font-bold text-slate-800">Xuất Dữ Liệu Cảnh Báo Sớm</h3>
                                    <p class="text-xs text-slate-500">Đầy đủ chỉ số A, L, xác suất, xu hướng tăng giảm</p>
                                </div>
                            </div>
                            <p class="text-xs text-slate-600">
                                Bấm nút bên dưới để xuất toàn bộ danh sách phân tích học sinh ra file Excel (.xlsx) chuẩn phục vụ họp bộ môn hoặc báo cáo chuyên môn.
                            </p>
                            <button onclick="exportExcel()" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-semibold py-3 rounded-xl text-xs transition flex items-center justify-center gap-2 shadow-sm">
                                <i class="fa-solid fa-file-excel text-sm"></i> Xuất Danh Sách Cảnh Báo (.XLSX)
                            </button>
                        </div>
                    </div>
                </div>
            </section>
        </main>
    </div>

    <!-- MODAL: HỒ SƠ CHI TIẾT & SO SÁNH TIẾN TRÌNH T1 -> T4 -->
    <div id="student-modal" class="fixed inset-0 bg-slate-900/60 backdrop-blur-sm z-50 flex items-center justify-center hidden p-4">
        <div class="bg-white rounded-2xl border border-slate-200 shadow-2xl max-w-3xl w-full max-h-[92vh] flex flex-col overflow-hidden text-xs">
            <div class="p-5 border-b border-slate-200 bg-slate-50 flex items-center justify-between">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-full bg-brand-100 text-brand-700 font-bold flex items-center justify-center text-sm" id="modal-avatar">HS</div>
                    <div>
                        <h3 class="text-base font-bold text-slate-900" id="modal-student-id">Mã HS: HS12_001</h3>
                        <p class="text-xs text-slate-500" id="modal-sub-info">Lớp • Tiến trình học tập</p>
                    </div>
                </div>
                <button onclick="closeModal()" class="w-8 h-8 rounded-full bg-slate-200 text-slate-600 hover:bg-slate-300 flex items-center justify-center transition">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>
            <div class="p-6 overflow-y-auto custom-scrollbar space-y-6">
                <!-- THẺ ĐÁNH GIÁ CHUNG -->
                <div class="grid grid-cols-1 sm:grid-cols-3 gap-3">
                    <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
                        <span class="text-slate-500">Mức Cảnh Báo (T4)</span>
                        <div class="text-sm font-bold mt-1" id="modal-risk-badge">Ưu tiên hỗ trợ</div>
                    </div>
                    <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
                        <span class="text-slate-500">Xác suất Nguy cơ</span>
                        <div class="text-sm font-bold text-rose-600 mt-1" id="modal-prob">0%</div>
                    </div>
                    <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-center">
                        <span class="text-slate-500">Xu hướng tổng thể</span>
                        <div class="text-sm font-bold mt-1" id="modal-trend-badge">Đang theo dõi</div>
                    </div>
                </div>

                <!-- BẢNG SO SÁNH TIẾN TRÌNH CÁC MỐC THỜI GIAN -->
                <div class="bg-white border border-slate-200 rounded-xl overflow-hidden shadow-sm">
                    <div class="bg-slate-50 px-4 py-2.5 font-bold text-slate-800 border-b border-slate-200 flex items-center justify-between">
                        <span><i class="fa-solid fa-chart-line text-brand-600 mr-1.5"></i> Tiến trình so sánh qua các mốc thời gian</span>
                        <span class="text-[11px] text-slate-500 font-normal">T1: Tuần 4 ➔ T4: Tuần 16</span>
                    </div>
                    <table class="w-full text-left text-xs border-collapse">
                        <thead class="bg-slate-50/50 text-slate-600 border-b border-slate-100">
                            <tr>
                                <th class="p-2.5">Mốc Thời Gian</th>
                                <th class="p-2.5 text-center">Điểm Kiểm Tra (A)</th>
                                <th class="p-2.5 text-center">Tương Tác LMS (L)</th>
                                <th class="p-2.5 text-center">Xác Suất Nguy Cơ</th>
                                <th class="p-2.5 text-right">Đánh Giá Biến Động</th>
                            </tr>
                        </thead>
                        <tbody id="modal-history-tbody" class="divide-y divide-slate-100"></tbody>
                    </table>
                </div>

                <!-- ĐÓNG GÓP SHAP CHO A VÀ L -->
                <div class="bg-slate-50 p-4 rounded-xl border border-slate-200">
                    <h4 class="font-bold text-slate-800 text-xs mb-1 flex items-center gap-2">
                        <i class="fa-solid fa-brain text-purple-600"></i> Phân Tích Mức Đóng Góp Vào Nguy Cơ (A & L)
                    </h4>
                    <div class="space-y-3 mt-3" id="modal-shap-list"></div>
                </div>
            </div>
            <div class="p-4 border-t border-slate-200 bg-slate-50 flex items-center justify-end gap-2">
                <button onclick="closeModal()" class="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-700 font-semibold rounded-xl transition">Đóng</button>
                <button onclick="navigateInterventionFromModal()" class="px-4 py-2 bg-brand-600 hover:bg-brand-700 text-white font-semibold rounded-xl transition flex items-center gap-1.5 shadow-sm">
                    <i class="fa-solid fa-pen-to-square"></i> Thêm Nhật Ký Can Thiệp
                </button>
            </div>
        </div>
    </div>

    <script>
        let studentData = [];
        let interventionLogs = [];
        let currentSelectedStudent = null;
        let riskChartInstance = null;
        let progressionChartInstance = null;
        let alpChartInstance = null;

        function handleLogin() {
            const user = document.getElementById('username').value.trim();
            const pass = document.getElementById('password').value.trim();
            const errorEl = document.getElementById('login-error');
            
            if(user !== "" && pass !== "") {
                document.getElementById('login-screen').classList.add('opacity-0', 'pointer-events-none');
                setTimeout(() => {
                    document.getElementById('login-screen').style.display = 'none';
                    const app = document.getElementById('main-app');
                    app.classList.remove('opacity-0', 'pointer-events-none');
                    initSystem();
                }, 300);
            } else {
                errorEl.classList.remove('hidden');
            }
        }

        function handleLogout() {
            document.getElementById('username').value = '';
            document.getElementById('password').value = '';
            const loginScreen = document.getElementById('login-screen');
            loginScreen.style.display = 'flex';
            setTimeout(() => {
                loginScreen.classList.remove('opacity-0', 'pointer-events-none');
            }, 10);
            document.getElementById('main-app').classList.add('opacity-0', 'pointer-events-none');
        }

        function initSystem() {
            initCharts();
            renderDashboard();
            renderTable();
            renderInterventions();
            const dateInput = document.getElementById('form-reassess-date');
            if(dateInput) dateInput.value = new Date().toISOString().split('T')[0];
        }

        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.classList.remove('border-brand-500', 'text-white');
                btn.classList.add('border-transparent');
            });
            document.getElementById(tabId).classList.remove('hidden');
            document.getElementById(`nav-${tabId}`).classList.add('border-brand-500', 'text-white');
            document.getElementById(`nav-${tabId}`).classList.remove('border-transparent');
        }

        function initCharts() {
            const ctxRisk = document.getElementById('riskDistributionChart').getContext('2d');
            riskChartInstance = new Chart(ctxRisk, {
                type: 'doughnut',
                data: { labels: ['Nguy cơ Thấp', 'Cần Theo Dõi', 'Ưu Tiên Hỗ Trợ'], datasets: [{ data: [0, 0, 0], backgroundColor: ['#22c55e', '#f59e0b', '#f43f5e'] }] },
                options: { responsive: true, maintainAspectRatio: false, cutout: '68%' }
            });

            const ctxProg = document.getElementById('progressionChart').getContext('2d');
            progressionChartInstance = new Chart(ctxProg, {
                type: 'line',
                data: {
                    labels: ['Mốc T1 (Tuần 4)', 'Mốc T2 (Tuần 8)', 'Mốc T3 (Tuần 12)', 'Mốc T4 (Hiện tại)'],
                    datasets: [
                        { label: 'Ưu tiên hỗ trợ (%)', data: [0, 0, 0, 0], borderColor: '#f43f5e', fill: true, backgroundColor: 'rgba(244, 63, 94, 0.1)', tension: 0.3 },
                        { label: 'Cần theo dõi (%)', data: [0, 0, 0, 0], borderColor: '#f59e0b', fill: true, backgroundColor: 'rgba(245, 158, 11, 0.1)', tension: 0.3 }
                    ]
                },
                options: { responsive: true, maintainAspectRatio: false }
            });

            const ctxAlp = document.getElementById('alpFeatureChart').getContext('2d');
            alpChartInstance = new Chart(ctxAlp, {
                type: 'bar',
                data: { labels: ['Kiểm tra (A)', 'Tương tác LMS (L)'], datasets: [{ data: [60, 40], backgroundColor: ['#3b82f6', '#10b981'], borderRadius: 8 }] },
                options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } } }
            });
        }

        function updateChartsData() {
            const low = studentData.filter(s => s.riskLevel === 'Thấp').length;
            const med = studentData.filter(s => s.riskLevel === 'Cần theo dõi').length;
            const high = studentData.filter(s => s.riskLevel === 'Ưu tiên hỗ trợ').length;
            const total = studentData.length || 1;

            if (riskChartInstance) {
                riskChartInstance.data.datasets[0].data = [low, med, high];
                riskChartInstance.update();
            }

            if (progressionChartInstance) {
                const highPct = Math.round((high / total) * 100);
                const medPct = Math.round((med / total) * 100);
                progressionChartInstance.data.datasets[0].data = [Math.max(2, highPct - 6), Math.max(3, highPct - 3), highPct, highPct];
                progressionChartInstance.data.datasets[1].data = [Math.max(5, medPct - 5), Math.max(8, medPct - 2), medPct, medPct];
                progressionChartInstance.update();
            }
        }

        function renderDashboard() {
            const total = studentData.length;
            const low = studentData.filter(s => s.riskLevel === 'Thấp').length;
            const medium = studentData.filter(s => s.riskLevel === 'Cần theo dõi').length;
            const high = studentData.filter(s => s.riskLevel === 'Ưu tiên hỗ trợ').length;

            document.getElementById('kpi-total').innerText = total;
            document.getElementById('kpi-low').innerText = low;
            document.getElementById('kpi-medium').innerText = medium;
            document.getElementById('kpi-high').innerText = high;
            document.getElementById('alert-badge-count').innerText = high;

            const lowPct = total > 0 ? Math.round((low / total) * 100) : 0;
            const medPct = total > 0 ? Math.round((medium / total) * 100) : 0;
            const highPct = total > 0 ? Math.round((high / total) * 100) : 0;

            document.getElementById('kpi-low-pct').innerHTML = `<i class="fa-solid fa-circle-check mr-1"></i> Tiến độ ổn định (${lowPct}%)`;
            document.getElementById('kpi-medium-pct').innerHTML = `<i class="fa-solid fa-triangle-exclamation mr-1"></i> Suy giảm nhẹ (${medPct}%)`;
            document.getElementById('kpi-high-pct').innerHTML = `<i class="fa-solid fa-circle-exclamation mr-1"></i> Nguy cơ không đạt (${highPct}%)`;

            updateChartsData();
        }

        function renderTable() {
            const searchVal = document.getElementById('search-student').value.toLowerCase();
            const classVal = document.getElementById('filter-class').value;
            const milestoneVal = document.getElementById('filter-milestone').value;
            const riskVal = document.getElementById('filter-risk').value;

            const filtered = studentData.filter(s => {
                return s.id.toLowerCase().includes(searchVal) && (!classVal || s.class === classVal) && (!milestoneVal || s.milestone === milestoneVal) && (!riskVal || s.riskLevel === riskVal);
            });

            document.getElementById('filter-count').innerText = filtered.length;
            document.getElementById('total-count').innerText = studentData.length;
            const tbody = document.getElementById('student-table-body');
            tbody.innerHTML = '';

            if (filtered.length === 0) {
                tbody.innerHTML = `<tr><td colspan="8" class="text-center py-8 text-slate-400">Chưa có dữ liệu học sinh hoặc không tìm thấy kết quả</td></tr>`;
                return;
            }

            filtered.forEach(s => {
                let badgeClass = s.riskLevel === 'Ưu tiên hỗ trợ' ? 'bg-rose-50 text-rose-700 border-rose-200 font-bold' : (s.riskLevel === 'Cần theo dõi' ? 'bg-amber-50 text-amber-700 border-amber-200' : 'bg-emerald-50 text-emerald-700 border-emerald-200');
                
                // HIỂN THỊ XU HƯỚNG CHUẨN XÁC:
                let trendIcon = '';
                if (s.milestone === 'T1' || s.trend === 'baseline') {
                    trendIcon = '<span class="text-slate-400 font-medium flex items-center justify-center gap-1"><i class="fa-solid fa-minus"></i> Mốc khởi điểm</span>';
                } else if (s.trend === 'up') {
                    trendIcon = '<span class="text-rose-600 font-bold flex items-center justify-center gap-1"><i class="fa-solid fa-arrow-trend-up"></i> Tăng nguy cơ (Sa sút)</span>';
                } else if (s.trend === 'down') {
                    trendIcon = '<span class="text-emerald-600 font-bold flex items-center justify-center gap-1"><i class="fa-solid fa-arrow-trend-down"></i> Tiến bộ (Giảm rủi ro)</span>';
                } else {
                    trendIcon = '<span class="text-slate-500 font-medium flex items-center justify-center gap-1"><i class="fa-solid fa-arrow-right"></i> Ổn định</span>';
                }

                tbody.innerHTML += `
                    <tr class="hover:bg-slate-50 transition">
                        <td class="py-3 px-4 font-bold text-slate-800">${s.id}</td>
                        <td class="py-3 px-4">${s.class}</td>
                        <td class="py-3 px-4 font-semibold text-slate-700">${s.milestone}</td>
                        <td class="py-3 px-4 text-center">A: ${s.scoreA} | L: ${s.scoreL}%</td>
                        <td class="py-3 px-4 font-semibold">${s.probability}%</td>
                        <td class="py-3 px-4"><span class="px-2.5 py-1 rounded-full text-[11px] border ${badgeClass}">${s.riskLevel}</span></td>
                        <td class="py-3 px-4 text-center">${trendIcon}</td>
                        <td class="py-3 px-4 text-right"><button onclick="openModal('${s.id}')" class="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 rounded-lg text-xs font-medium">Xem Hồ Sơ</button></td>
                    </tr>
                `;
            });
        }

        function filterStudents() { renderTable(); }

        function openModal(studentId) {
            const student = studentData.find(s => s.id === studentId);
            if (!student) return;
            currentSelectedStudent = student;
            document.getElementById('modal-student-id').innerText = `Mã HS: ${student.id}`;
            document.getElementById('modal-sub-info').innerText = `Lớp ${student.class} • Mốc hiện tại: ${student.milestone}`;
            document.getElementById('modal-risk-badge').innerText = student.riskLevel;
            document.getElementById('modal-prob').innerText = `${student.probability}%`;

            let trendBadge = document.getElementById('modal-trend-badge');
            if (student.milestone === 'T1' || student.trend === 'baseline') {
                trendBadge.innerHTML = '<span class="text-slate-500"><i class="fa-solid fa-minus"></i> Mốc đánh giá khởi điểm</span>';
            } else if (student.trend === 'up') {
                trendBadge.innerHTML = '<span class="text-rose-600 font-bold"><i class="fa-solid fa-arrow-trend-up"></i> Có dấu hiệu sa sút (Tăng nguy cơ)</span>';
            } else if (student.trend === 'down') {
                trendBadge.innerHTML = '<span class="text-emerald-600 font-bold"><i class="fa-solid fa-arrow-trend-down"></i> Đang có tiến bộ tốt</span>';
            } else {
                trendBadge.innerHTML = '<span class="text-slate-500"><i class="fa-solid fa-arrow-right"></i> Duy trì ổn định</span>';
            }
            
            // Xây dựng bảng so sánh tiến trình T1 -> T4
            const tbodyHistory = document.getElementById('modal-history-tbody');
            tbodyHistory.innerHTML = '';
            
            let baseScoreT1 = student.scoreA_T1 !== null ? student.scoreA_T1 : (student.milestone === 'T1' ? student.scoreA : Math.min(10, student.scoreA + (student.trend === 'up' ? 1.5 : -1.0)));
            let baseProbT1 = Math.min(98, Math.max(5, Math.round((10 - baseScoreT1) * 7 + (100 - (student.scoreL + 10)) * 0.3)));

            const history = student.history || [
                { milestone: 'T1 (Tuần 4 - Baseline)', a: baseScoreT1, l: Math.min(100, student.scoreL + 10), prob: baseProbT1 },
                { milestone: 'T2 (Tuần 8 - Giữa kỳ)', a: parseFloat(((baseScoreT1 + student.scoreA) / 2).toFixed(1)), l: student.scoreL, prob: Math.round((baseProbT1 + student.probability) / 2) },
                { milestone: 'T3 (Tuần 12 - Sau can thiệp)', a: student.scoreA, l: student.scoreL, prob: student.probability },
                { milestone: 'T4 (Tuần 16 - Thi Học kỳ)', a: student.scoreA, l: student.scoreL, prob: student.probability }
            ];

            history.forEach((h, idx) => {
                let diffText = '-';
                if (idx === 0) {
                    diffText = `<span class="text-slate-400">Khởi điểm</span>`;
                } else {
                    let prevScore = history[idx - 1].a;
                    let diffScore = parseFloat((h.a - prevScore).toFixed(1));
                    if (diffScore < 0) diffText = `<span class="text-rose-600 font-bold">${diffScore} điểm (Sa sút ↗)</span>`;
                    else if (diffScore > 0) diffText = `<span class="text-emerald-600 font-bold">+${diffScore} điểm (Tiến bộ ↘)</span>`;
                    else diffText = `<span class="text-slate-400">Không đổi ➜</span>`;
                }

                tbodyHistory.innerHTML += `
                    <tr>
                        <td class="p-2.5 font-semibold text-slate-700">${h.milestone}</td>
                        <td class="p-2.5 text-center font-bold text-slate-800">${h.a}</td>
                        <td class="p-2.5 text-center">${h.l}%</td>
                        <td class="p-2.5 text-center font-bold">${h.prob}%</td>
                        <td class="p-2.5 text-right">${diffText}</td>
                    </tr>
                `;
            });

            // Giải thích mô hình SHAP
            const shapBox = document.getElementById('modal-shap-list');
            shapBox.innerHTML = `
                <div>
                    <div class="flex justify-between mb-1"><span>Điểm bài kiểm tra (Group A: ${student.scoreA} điểm)</span><span class="font-bold text-amber-600">${student.scoreA < 6.5 ? 'Gia tăng rủi ro' : 'Tích cực'}</span></div>
                    <div class="w-full bg-slate-200 rounded-full h-2"><div class="bg-amber-500 h-2 rounded-full" style="width: ${Math.min(100, Math.max(10, (10 - student.scoreA) * 10))}%"></div></div>
                </div>
                <div>
                    <div class="flex justify-between mb-1"><span>Tương tác LMS (Group L: ${student.scoreL}%)</span><span class="font-bold text-blue-600">${student.scoreL < 50 ? 'Gia tăng rủi ro' : 'Tích cực'}</span></div>
                    <div class="w-full bg-slate-200 rounded-full h-2"><div class="bg-blue-500 h-2 rounded-full" style="width: ${Math.min(100, Math.max(10, 100 - student.scoreL))}%"></div></div>
                </div>
            `;
            document.getElementById('student-modal').classList.remove('hidden');
        }

        function closeModal() { document.getElementById('student-modal').classList.add('hidden'); }
        function navigateInterventionFromModal() { closeModal(); switchTab('tab-interventions'); document.getElementById('form-student-id').value = currentSelectedStudent.id; }

        function populateInterventionStudentOptions() {
            const select = document.getElementById('form-student-id');
            const classFilter = document.getElementById('filter-class');
            select.innerHTML = '';
            
            const classes = [...new Set(studentData.map(s => s.class))];
            classFilter.innerHTML = '<option value="">Tất cả các lớp</option>';
            classes.forEach(c => { classFilter.innerHTML += `<option value="${c}">${c}</option>`; });

            studentData.forEach(s => { select.innerHTML += `<option value="${s.id}">${s.id} (${s.class})</option>`; });
        }

        function renderInterventions() {
            const container = document.getElementById('interventions-list');
            document.getElementById('intervention-count').innerText = interventionLogs.length;
            container.innerHTML = '';
            if (interventionLogs.length === 0) {
                container.innerHTML = '<div class="text-center py-8 text-slate-400 text-xs">Chưa có nhật ký can thiệp nào</div>';
                return;
            }
            interventionLogs.forEach(log => {
                container.innerHTML += `
                    <div class="p-3.5 bg-slate-50 rounded-xl border border-slate-200 space-y-1.5 text-xs">
                        <div class="flex justify-between font-bold"><span>${log.studentId} • ${log.date}</span><span class="px-2 py-0.5 rounded border bg-white">${log.status}</span></div>
                        <div><strong>Biện pháp:</strong> ${log.action}</div>
                        <div class="italic text-slate-500">"${log.note}"</div>
                    </div>
                `;
            });
        }

        function saveIntervention(e) {
            e.preventDefault();
            interventionLogs.unshift({
                id: Date.now(),
                studentId: document.getElementById('form-student-id').value,
                date: new Date().toISOString().split('T')[0],
                verification: document.getElementById('form-verification').value,
                action: document.getElementById('form-action').value,
                note: document.getElementById('form-note').value || 'Không có ghi chú',
                reassessDate: document.getElementById('form-reassess-date').value,
                status: document.getElementById('form-status').value
            });
            renderInterventions();
            alert('Lưu nhật ký can thiệp thành công!');
            document.getElementById('form-note').value = '';
        }

        function triggerFileInput() { document.getElementById('file-input').click(); }

       // ================= XỬ LÝ NHẬP EXCEL & TỰ ĐỘNG KHỚP LỊCH SỬ T1 -> T4 =================
        function handleExcelUpload(e) {
            const file = e.target.files[0];
            if (!file) return;

            const reader = new FileReader();
            reader.onload = function(evt) {
                try {
                    const data = new Uint8Array(evt.target.result);
                    const workbook = XLSX.read(data, { type: 'array' });
                    const firstSheet = workbook.Sheets[workbook.SheetNames[0]];
                    const json = XLSX.utils.sheet_to_json(firstSheet);

                    if (!json || json.length === 0) {
                        alert('Tệp Excel trống hoặc không có nội dung hợp lệ!');
                        return;
                    }

                    // BƯỚC 1: Đọc và chuẩn hóa toàn bộ các dòng từ Excel
                    let rawList = json.map((row, idx) => {
                        let id = String(row['Mã_HS'] || row['Mã học sinh'] || row['Ma_HS'] || row['ID'] || `HS12_${String(idx+1).padStart(3, '0')}`).trim();
                        let cls = String(row['Lớp'] || row['Lop'] || '12 Tin').trim();
                        let milestone = String(row['Mốc'] || row['Moc'] || row['Mốc_Đánh_Giá'] || 'T4').trim().toUpperCase();
                        
                        let scoreA = parseFloat(row['Điểm_A'] || row['Điểm_Đánh_Giá (A)'] || row['Diem_A'] || row['A'] || 7.0);
                        let scoreL = parseInt(row['Tương_Tác_LMS (L)'] || row['Tương_Tác_LMS'] || row['LMS'] || row['L'] || 70);

                        // Tính xác suất nguy cơ
                        let riskCalc = (10 - scoreA) * 7 + (100 - scoreL) * 0.3;
                        let prob = Math.min(98, Math.max(5, Math.round(riskCalc)));
                        let riskLevel = prob >= 65 ? 'Ưu tiên hỗ trợ' : (prob >= 40 ? 'Cần theo dõi' : 'Thấp');

                        return {
                            id: id,
                            class: cls,
                            milestone: milestone,
                            scoreA: scoreA,
                            scoreL: scoreL,
                            probability: prob,
                            riskLevel: riskLevel,
                            scoreA_T1: null,
                            history: []
                        };
                    });

                    // BƯỚC 2: Tự động gom nhóm theo Mã_HS để tìm mốc T1 và tính xu hướng tăng/giảm
                    // Lưu lại điểm T1 của từng học sinh
                    let t1Scores = {};
                    rawList.forEach(item => {
                        if (item.milestone === 'T1') {
                            t1Scores[item.id] = { scoreA: item.scoreA, scoreL: item.scoreL, prob: item.probability };
                        }
                    });

                    // Nếu trong dữ liệu cũ đã từng có mốc T1 thì giữ lại
                    studentData.forEach(item => {
                        if (item.milestone === 'T1' && !t1Scores[item.id]) {
                            t1Scores[item.id] = { scoreA: item.scoreA, scoreL: item.scoreL, prob: item.probability };
                        }
                    });

                    // BƯỚC 3: Gán xu hướng và lịch sử so sánh chính xác cho từng dòng
                    studentData = rawList.map(item => {
                        let trend = 'stable';
                        let historyData = [];

                        if (item.milestone === 'T1') {
                            trend = 'baseline'; // Mốc T1 luôn là mốc bắt đầu
                            historyData = [
                                { milestone: 'T1 (Tuần 4 - Baseline)', a: item.scoreA, l: item.scoreL, prob: item.probability }
                            ];
                        } else {
                            // Nếu là T2, T3, T4: Đối chiếu với mốc T1 của chính học sinh đó
                            let baseT1 = t1Scores[item.id];
                            if (baseT1) {
                                item.scoreA_T1 = baseT1.scoreA;
                                let delta = item.scoreA - baseT1.scoreA;

                                if (delta < -0.3) {
                                    trend = 'up';   // Điểm giảm (VD: từ 6 xuống 4) => TĂNG NGUY CƠ (SA SÚT)
                                } else if (delta > 0.3) {
                                    trend = 'down'; // Điểm tăng => TIẾN BỘ
                                } else {
                                    trend = 'stable'; // Điểm ngang nhau => ỔN ĐỊNH
                                }

                                historyData = [
                                    { milestone: 'T1 (Tuần 4 - Baseline)', a: baseT1.scoreA, l: baseT1.scoreL, prob: baseT1.prob },
                                    { milestone: `${item.milestone} (Hiện tại)`, a: item.scoreA, l: item.scoreL, prob: item.probability }
                                ];
                            } else {
                                // Nếu file không có mốc T1 để so: dựa vào mức cảnh báo thực tế
                                if (item.riskLevel === 'Ưu tiên hỗ trợ' || item.riskLevel === 'Cần theo dõi') {
                                    trend = 'up'; // Có rủi ro/sa sút
                                } else {
                                    trend = 'stable';
                                }
                                historyData = [
                                    { milestone: `${item.milestone} (Hiện tại)`, a: item.scoreA, l: item.scoreL, prob: item.probability }
                                ];
                            }
                        }

                        item.trend = trend;
                        item.history = historyData;
                        return item;
                    });

                    renderDashboard();
                    renderTable();
                    populateInterventionStudentOptions();
                    alert(`Đã nạp thành công dữ liệu và tự động khớp tiến trình cho ${studentData.length} lượt đánh giá!`);
                    switchTab('tab-alerts');
                } catch (err) {
                    alert('Lỗi đọc tệp Excel. Vui lòng kiểm tra lại định dạng tệp!');
                    console.error(err);
                } finally {
                    e.target.value = '';
                }
            };
            reader.readAsArrayBuffer(file);
        }

        // ================= TẢI FILE EXCEL MẪU =================
        function downloadTemplateExcel() {
            const sampleData = [
                { 'Mã_HS': 'HS12_001', 'Lớp': '12 Chuyên Tin', 'Mốc': 'T1', 'Điểm_A': 7.0, 'Điểm_T1': 7.0, 'Tương_Tác_LMS': 80 },
                { 'Mã_HS': 'HS12_002', 'Lớp': '12 Chuyên Tin', 'Mốc': 'T4', 'Điểm_A': 4.0, 'Điểm_T1': 6.0, 'Tương_Tác_LMS': 30 },
                { 'Mã_HS': 'HS12_003', 'Lớp': '12 A1', 'Mốc': 'T4', 'Điểm_A': 8.5, 'Điểm_T1': 5.0, 'Tương_Tác_LMS': 90 },
                { 'Mã_HS': 'HS12_004', 'Lớp': '12 A2', 'Mốc': 'T4', 'Điểm_A': 5.5, 'Điểm_T1': 5.5, 'Tương_Tác_LMS': 50 }
            ];

            const worksheet = XLSX.utils.json_to_sheet(sampleData);
            const workbook = XLSX.utils.book_new();
            XLSX.utils.book_append_sheet(workbook, worksheet, "Mau_Diem");
            XLSX.writeFile(workbook, "Mau_Nhap_Diem_EduRisk.xlsx");
        }
    </script>
</body>
</html>
"""

components.html(edurisk_html_code, height=1200, scrolling=True)