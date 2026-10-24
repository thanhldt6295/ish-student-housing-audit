# ISH Student Housing — Audit theo từng ứng dụng

**Đọc hành trình trước, xem từng ứng dụng sau.** Mục tiêu là giúp sinh viên biết việc cần làm và giúp nhân viên xử lý hồ sơ, phòng ở, tiền thu trong cùng một hành trình.

Ngày kiểm tra: **23/10/2026 · Chỉ đọc production**. Bản chia sẻ công khai đã bỏ ảnh production và chi tiết định danh/giao dịch. Bản này tổ chức lại kết quả audit đã có; không có kiểm tra production mới. Phần chính tập trung vào các việc quan trọng nhất. Bằng chứng và phân tích sâu được thu gọn ở cuối.

## 0. Hành trình tổng thể — chuyện gì đang diễn ra?

**Application Form** nhận hồ sơ → **Admin** xét duyệt và xử lý chỗ ở → **Student Portal** giúp sinh viên theo dõi, hoàn tất yêu cầu và thanh toán. Admin tiếp tục quản lý giá, hóa đơn và các yêu cầu trong suốt thời gian lưu trú.

Đây là **luồng mục tiêu đề xuất** để thiết kế và kể chuyện. Đã kiểm tra các màn và dữ liệu, nhưng chưa tái hiện toàn bộ việc gửi đơn, duyệt, xếp phòng và thanh toán.

| Bước | Ai làm và ở đâu? | Kết quả cần thấy | Ai nhận việc tiếp theo? |
|---|---|---|---|
| J01 — Đăng ký | Sinh viên · Application Form | Đơn đã gửi; kết quả phí xét đơn tách riêng | Admin nhận hồ sơ |
| J02 — Xét duyệt | Nhân viên · Admin | Được nhận, cần bổ sung hoặc chờ chỗ | Sinh viên nhận hướng dẫn |
| J03 — Hoàn tất điều kiện | Sinh viên · Portal, điểm vào cần xác nhận | Giấy tờ, thỏa thuận và điều kiện đã hoàn tất; biết hạn giữ chỗ | Admin kiểm tra và xử lý chỗ ở |
| J04 — Chọn/xác nhận chỗ ở | Admin xếp phòng hoặc sinh viên chọn trong Portal theo quyền | Phòng/bed, ngày ở, giá và trạng thái rõ ràng | Sinh viên xem trong Portal |
| J05 — Phát hành hóa đơn | Nhân viên · Admin | Khoản được phát hành có kỳ thu và hạn trả | Sinh viên nhận việc cần thanh toán |
| J06 — Thanh toán | Sinh viên · Portal | Đang xử lý, thành công hoặc thất bại; biên nhận khi thành công | Admin theo dõi và đối soát |
| J07 — Trong thời gian ở | Sinh viên · Portal; nhân viên · Admin | Xem tài liệu, gửi và theo dõi yêu cầu | Bên phụ trách xử lý và phản hồi |

**Ba điều phải hiểu đúng:** Nộp đơn chưa đồng nghĩa có phòng. Giá dự kiến chưa đồng nghĩa khoản đang phải trả. Một sinh viên có thể có nhiều lần đặt phòng, nên tiền và giấy tờ phải gắn đúng lần ở.

### Bổ sung ngày 24/10 — cần tách hai cách đặt phòng

**Làm rõ từ trao đổi với người phụ trách:** application được admin từ chối hoặc chuyển thành reservation. Có một use case riêng: sau khi được duyệt, sinh viên có thể tự chọn phòng trong Portal; đây không phải Request Room Change. Chưa xác nhận use case này đang bật trên ISH hiện tại hoặc thời điểm gửi tài khoản Portal.

**Đã thấy trong file Figma Student Portal cũ:** màn New Reservation có Booking Term, thẻ loại phòng, ảnh, giá, tiện nghi, Select và Proceed. Đây là ảnh tham chiếu trong page OLD; page NEW Design đang trống. Bằng chứng này bổ sung nguồn thiết kế, không chứng minh chức năng đang hoạt động trên production. [F05]

**Ảnh hưởng:** J04 cần hỗ trợ hai nhánh theo cấu hình: admin xếp phòng hoặc sinh viên được phép chọn phòng sau duyệt. Giữ bước xem giá/xác nhận và trạng thái sau đặt. Video có thể kể nhánh sinh viên tự chọn phòng khi nhánh đó được kiểm chứng.

### Một hồ sơ mẫu để nối tất cả màn hình

Dùng **Alex Morgan — Demo House — Fall Demo 2027** trong thiết kế và video. Đây là dữ liệu giả đề xuất. Cùng một mã hồ sơ, reservation, phòng, ngày ở và bộ hóa đơn xuất hiện ở cả ba ứng dụng. Giá và lịch thu mẫu cần thống nhất sau khi Finance xác nhận quy tắc.

### Cách đọc bằng chứng

**Đã xác minh:** nhìn thấy trực tiếp trong production/Figma. **Cần xác nhận:** chưa kiểm tra được hành vi hoặc quy tắc. **Đề xuất:** trải nghiệm nên thiết kế. Mã E là bằng chứng production, F là Figma, V là mô tả video; tra ở cuối tài liệu.

## 1. Application Form — sinh viên bắt đầu đăng ký

**Ai dùng?** Người muốn đăng ký ở. **Họ cần biết:** có phù hợp không, cần chuẩn bị gì, phí bao nhiêu và gửi xong thì chuyện gì xảy ra.

**Đầu vào:** nhu cầu và thời gian lưu trú. **Đầu ra:** hồ sơ chuyển sang Admin để xét duyệt, kèm kết quả phí đăng ký. Liên kết hành trình: **J01 → J02**.

### Hiện tại

Trang đầu giải thích admissions, phí không hoàn lại, xử lý tối đa 2 ngày làm việc và bước hoàn tất điều kiện trong 5 ngày sau acceptance. Có waitlist nếu không đủ chỗ. Form có 6 bước; đã xem thông tin cá nhân và màn phí $50. Chưa kiểm tra bước 2–5 hoặc gửi đơn. [E01–E03]

### Những việc cần sửa trước

| Cần làm | Vì sao? | Kết quả mong muốn |
|---|---|---|
| Đặt tên từng bước, nói rõ giấy tờ và phí từ đầu | Sinh viên biết cần chuẩn bị gì | Hiểu quy trình mà không cần nhân viên giải thích |
| Có màn xem lại trước khi trả phí và gửi | Tránh hiểu trả phí là chắc chắn có phòng | Phí, thông tin đã nhập và bước tiếp theo đều rõ |
| Có kết quả gửi và hướng xử lý khi lỗi | Tránh không biết đơn đã gửi hay tiền đã trả chưa | Có mã tham chiếu; phân biệt kết quả phí với kết quả gửi đơn |

### Luồng và màn hình nên thiết kế

Hướng dẫn trước đăng ký → các bước có tên → xem lại → trả phí/gửi → kết quả → theo dõi hồ sơ. Nối thông tin sang Admin và Portal, không bắt nhập lại.

Các màn chính: Before you apply; form; Review & fee; kết quả thành công/đang xử lý/thất bại; hướng dẫn theo dõi. Chi tiết inventory: A01–A09 trong file màn hình đi kèm.

**Cần xác nhận:** bước 2–5, lưu và tiếp tục, lúc tạo reservation và cấp tài khoản Portal. Chưa mặc định application là reservation đã được xác nhận.

**Bàn giao sang Admin:** nhân viên nhận đúng hồ sơ và kết quả phí, biết còn thiếu gì. **Cảnh video:** Alex đăng ký và nhận mã hồ sơ → nhân viên mở chính hồ sơ đó.

## 2. Student Management — nhân viên quản lý và xử lý

**Ai dùng?** Admissions, đội xếp phòng và Finance. **Họ cần biết:** ai đang chờ xử lý, thiếu gì, còn chỗ không và khoản tiền nào cần phát hành/đối soát.

**Đầu vào:** hồ sơ từ Application Form; giấy tờ và yêu cầu từ Portal. **Đầu ra:** kết quả xét duyệt, chỗ ở, hóa đơn và phản hồi cho sinh viên. Liên kết hành trình: **J02, J04, J05 và phần xử lý J07**.

### Hiện tại

Có Resident Applications, Reservations, Availability, Rate Controller và BN Invoices. Reservation có room/bed, ngày ở, tổng tiền, deposit và hóa đơn liên quan. Có invoice Draft/Partial/Paid; rate manager có Nightly/X Nights/Monthly. Chưa thử duyệt, gán phòng, đổi giá hay phát hành hóa đơn. [E07–E10, E14–E16]

### Những việc cần sửa trước

| Cần làm | Vì sao? | Kết quả mong muốn |
|---|---|---|
| Danh sách hồ sơ chờ xử lý, thiếu giấy tờ, sắp hết hạn | View application đã xem chỉ có mã | Biết cần xử lý ai và việc gì trước |
| Từ hồ sơ xem được reservation, phòng, giá, hóa đơn và payment | Tránh tìm lại và nhầm giữa nhiều lần ở | Mở phần liên quan mà vẫn giữ đúng ngữ cảnh |
| Xếp phòng có ngày ở, tình trạng còn chỗ và giá đi kèm | Tránh xác nhận khi thiếu thông tin | Xem kết quả và xung đột trước khi xác nhận |
| Rõ quy trình kiểm tra → phát hành hóa đơn → đối soát | Sinh viên nhận đúng khoản phải trả | Trạng thái, số tiền và lịch sử khớp giữa hai phía |

### Luồng và màn hình nên thiết kế

Nhận hồ sơ → kiểm tra → chấp thuận/chờ chỗ/yêu cầu bổ sung → kiểm tra điều kiện giữ chỗ → xác nhận phòng → kiểm tra giá/lịch thu → phát hành hóa đơn → theo dõi thanh toán. Thứ tự cụ thể giữa hồ sơ, hold và placement cần ISH xác nhận.

Các màn chính: Work queue; Application review; Reservation detail; Availability/placement; Rates và xem trước giá; Invoice list/detail/review; Payments/đối soát. Chi tiết inventory: D01–D09.

**Cần xác nhận trước khi làm phần tiền:** tính kỳ không trọn tháng, deposit áp dụng cho lần ở nào, semester/fixed-term, quyền duyệt và thời điểm sinh viên thấy hóa đơn. Một invoice mẫu có ngày và đơn vị giá cần Finance đối soát; chưa kết luận tính sai tiền. [E04, E06, E09, E10]

**Bàn giao sang Portal:** sinh viên thấy kết quả, việc cần làm và khoản được phép trả. Khi sinh viên trả tiền/gửi giấy tờ, admin thấy kết quả tương ứng. **Cảnh video:** nhân viên mở hồ sơ Alex, xác nhận chỗ ở, phát hành hóa đơn → Portal của Alex hiển thị kết quả.

## 3. Student Portal — sinh viên theo dõi và tự phục vụ

**Ai dùng?** Sinh viên đã có quyền truy cập. **Họ cần biết:** hồ sơ/chỗ ở ra sao, cần làm gì tiếp và cần trả bao nhiêu.

**Đầu vào:** kết quả xử lý từ Admin và thông tin lưu trú. **Đầu ra:** giấy tờ, thanh toán và yêu cầu gửi về đúng bộ phận. Liên kết hành trình: **J03, J06, J07**, cùng việc xem kết quả J02/J04/J05.

### Hiện tại

Có Dashboard, hai reservation trong tài khoản mẫu, lịch sử invoice/payment, yêu cầu khách qua đêm và thông tin cư dân. Figma đã có Payments, thêm phương thức thanh toán và mobile. Chưa thấy luồng đầy đủ cho reserve, invoice đến hạn và kết quả checkout trong inventory Figma đã xem. [E04–E06, E12–E13, F01–F04]

### Những việc cần sửa trước

| Cần làm | Vì sao? | Kết quả mong muốn |
|---|---|---|
| Đưa việc cần làm, hồ sơ/phòng, giấy tờ và tiền đến hạn lên đầu | Không phải tìm giữa news và map | Mở Home là biết bước tiếp theo |
| Phân biệt lần ở hiện tại, sắp tới và trước đây | Một người có nhiều reservation | Phòng, ngày ở, tiền và deposit luôn rõ thuộc lần ở nào |
| Hoàn chỉnh invoice → thanh toán → biên nhận | Có lịch sử chưa đủ để xử lý khoản phải trả | Biết trả cho kỳ nào, còn bao nhiêu, kết quả và cách xử lý lỗi |
| Giữ guest request, tài liệu, hỗ trợ và kiểm tra mobile | Đây là các việc thực tế trong thời gian ở | Handbook mở được; yêu cầu có trạng thái; luồng chính dùng được trên điện thoại |

### Luồng và màn hình nên thiết kế

Home hiển thị việc tiếp theo → mở checklist/reservation/invoice → hoàn thành việc → thấy kết quả → trở về Home với trạng thái mới. News và map ở dưới hoặc mục riêng.

**Ví dụ cần diễn đạt đúng:** portal tài khoản mẫu báo $0 trong khi admin có invoice Draft cho lần ở sắp tới. Chưa đủ bằng chứng kết luận sai số dư. Cần phân biệt tiền đang phải trả và chi phí dự kiến theo chính sách; không đưa invoice nháp lên Portal khi chưa được phép. [E05, E08, V01]

Các màn chính: Task home; Application status/checklist; Reservation list/detail; giá/lịch thu; Invoice list/detail; Checkout; processing/success/failure/receipt; Guests; Documents/Help. Chi tiết inventory: S01–S07, T01–T06, R01–R02.

**Cần xác nhận:** khi nào có tài khoản Portal; sinh viên được chọn phòng hay chỉ gửi nguyện vọng; payment/deposit policy; maintenance, scholarships và thay đổi hợp đồng đang có hay là bổ sung mới.

**Bàn giao về Admin:** mỗi giấy tờ, payment, yêu cầu có hồ sơ/reservation liên quan và người tiếp nhận. **Cảnh video:** Alex thấy đúng hóa đơn vừa phát hành, trả trong sandbox, nhận biên nhận → admin thấy kết quả giao dịch đó.

## 4. Việc chung và thứ tự thực hiện

**Ưu tiên:** đăng ký/xét duyệt → xếp phòng → giá/hóa đơn → thanh toán. Giữ đủ chức năng cũ. Các tính năng mới như scholarships, community nâng cao hoặc thay đổi hợp đồng cần xác nhận nhu cầu trước.

| Giai đoạn | Công việc | Kết quả |
|---|---|---|
| 1 — Chốt luồng | Xác nhận nghiệp vụ; dùng một hồ sơ mẫu nối ba ứng dụng | Ai làm gì, trạng thái nào, chuyển cho ai đều rõ |
| 2 — Thiết kế | Application, Admin và Portal; dùng chung component/dữ liệu mẫu | Đi xuyên J01–J07, có cả trường hợp lỗi và chờ |
| 3 — Làm và kiểm tra | Sandbox, đối soát tiền, kiểm tra quyền/mobile và chuyển dữ liệu | Không mất chức năng/liên kết; khoản thu và trạng thái đúng |
| 4 — Pilot và video | ISH dùng thử; quay luồng đã kiểm chứng với dữ liệu giả | Sẵn sàng giới thiệu và mở rộng khách hàng |

**Thiết kế dùng lại:** chung nút, form, bảng, trạng thái, tiền/ngày và mẫu màn. Logo, màu, kỳ ở, giá và chính sách cấu hình riêng theo khách. Admin và Portal phù hợp người dùng của mình nhưng dùng cùng khái niệm/dữ liệu.

**Trước phát hành cần kiểm tra:** không lẫn kết quả phí và gửi đơn; không thu trùng khi thử lại; deposit đúng lần ở; invoice đã trả không báo nợ quá hạn; sinh viên chỉ thấy dữ liệu được phép; chức năng cũ và lịch sử được giữ.

## 5. Nối thành câu chuyện video

Mỗi tập kể một việc hoàn chỉnh, có bắt đầu và kết quả. Chuyển ứng dụng khi người tiếp theo nhận việc; giữ cùng hồ sơ Alex, reservation, invoice và số tiền.

| Tập | Bắt đầu → kết thúc | Ứng dụng xuất hiện | Bước |
|---|---|---|---|
| 1 — Đăng ký và xét duyệt | Alex nộp đơn → nhận kết quả/hướng dẫn | Application → Admin → Portal nếu đã có tài khoản | J01–J02 |
| 2 — Từ được nhận đến có chỗ ở | Hoàn tất điều kiện → xác nhận phòng/ngày | Portal → Admin → Portal | J03–J04 |
| 3 — Từ hóa đơn đến biên nhận | Phát hành → Alex trả → nhân viên thấy kết quả | Admin → Portal → Admin | J05–J06 |
| 4 — Tự phục vụ khi đang ở | Tài liệu/guest request → trạng thái xử lý | Portal → Admin → Portal | J07 |
| 5 — Một gói cho nhiều cơ sở | Cùng luồng, đổi cấu hình và thương hiệu demo | Cấu hình và cả ba ứng dụng | Toàn hành trình |

Có thể làm thêm tập về giá sau khi xác nhận các mô hình monthly/semester/fixed-term. Storyboard chi tiết từ bản audit trước nằm bên dưới để tham khảo; danh sách tập ở trên là cách nhóm lại theo hành trình.

**Chỉ quay sandbox và dữ liệu giả.** Chưa triển khai thì ghi Prototype/Proposed experience. Không đưa credential, mã truy cập phòng, hồ sơ hoặc giao dịch production vào video.

## 6. Bằng chứng và phân tích chi tiết

Mở từng mục khi cần xem nguồn, inventory, thiết kế dùng lại hoặc storyboard. Đây là nội dung audit đã có, không phải nghiên cứu mới. Phần chính bên trên là cách đọc và tổ chức công việc được đề xuất mới.


:::details 1. Quyết định sản phẩm cần chốt

**Ưu tiên revamp toàn bộ chuỗi admissions → reservation/placement → rate → invoice → payment.** Dashboard mới là một phần của chuỗi đó. ISH có nghiệp vụ và dữ liệu liên kết đang hoạt động; thiết kế mới phải bảo toàn các liên kết và trạng thái trước khi bổ sung tính năng.

Ba điều chỉnh so với review được trích trong chat cũ:

1. **Application không thể mặc định đồng nghĩa với Reserve a Room.** Trang công khai mô tả quy trình admissions riêng: nộp đơn và phí không hoàn lại, chờ chấp thuận, sau đó hoàn thành hồ sơ để bảo đảm reservation. Danh sách Resident Applications tồn tại riêng trong Salesforce. [E01, E16]
2. **Figma có Payments và mobile.** Có Payment History, Receipt, Add New Payment Method, Dashboard và các màn mobile 393 px. Khoảng trống là các luồng hoàn chỉnh cho application, reservation, invoice phải trả và checkout; không phải hoàn toàn thiếu trang thanh toán. [F01–F04]
3. **$0 trong portal chưa chứng minh sai số dư.** Cùng reservation sắp tới có hai invoice Draft trong admin. Video mô tả sinh viên xem giao dịch đã duyệt. Thiếu lời giải thích về dự kiến/phải trả là vấn đề UX có cơ sở; lỗi đồng bộ hay lỗi thu tiền chưa được chứng minh. [E05, E08, V01]

Đề xuất release đầu: application và checklist sau chấp thuận; portal nhiệm vụ ưu tiên; reservation/placement workspace; mô hình giá rõ ràng; invoice có duyệt và payment states. Guests, handbook và thông tin thiết yếu phải được bảo toàn. Maintenance, scholarships, room change, renewal và termination cần phân loại theo bằng chứng trước khi đưa vào phạm vi.

:::enddetails

:::details 2. Phương pháp, bằng chứng và giới hạn

Ký hiệu dùng xuyên suốt:

| Nhãn | Ý nghĩa |
|---|---|
| **Đã xác minh** | Đã đọc trực tiếp production hoặc cấu trúc/nội dung Figma trong phiên này |
| **Nguồn mô tả** | Yêu cầu của người dùng hoặc mô tả/chapter video; chưa tái hiện hành vi |
| **Suy luận** | Giải thích hợp lý dựa trên các bằng chứng, cần xác nhận |
| **Đề xuất** | Thiết kế hoặc cấu hình mục tiêu; chưa triển khai |
| **Chưa kiểm tra** | Không có đủ quyền, trạng thái dữ liệu hoặc không thể thực hiện trong phạm vi chỉ đọc |

Có phiên portal và Salesforce đã đăng nhập sẵn. Không cần nhập lại credential. Chỉ điều hướng, mở modal, đổi tab và chạy tìm kiếm hiển thị. Không gửi application/guest request, không nhập thẻ, không thanh toán, không duyệt invoice, không thay rate, không check-in/out, không lưu/chỉnh bản ghi và không sửa Figma. Đọc production có thể tạo dấu vết truy cập/Recently Viewed thông thường của nền tảng; không có hành động ghi nghiệp vụ được chủ động thực hiện.

Mẫu kiểm tra gồm một tài khoản sinh viên với hai reservation, các invoice/payment liên quan, một danh sách reservation, rate manager/grid, availability, danh sách invoice và danh sách application. Đây là audit theo mẫu, không phải kiểm toán toàn bộ cơ sở dữ liệu.

Chưa kiểm tra: application bước 2–5; validation sau nhập; lưu nháp/tiếp tục; gửi đơn; duyệt/khước từ; placement và thay đổi trạng thái thực tế; checkout, thất bại/hoàn tiền; quyền của các role khác; email thông báo; tài liệu ID/hợp đồng cá nhân. Không tải hồ sơ nhận dạng hoặc dữ liệu hàng loạt.

Đã thử đặt viewport 393 × 852 nhưng trình duyệt vẫn báo chiều rộng thực tế 1440 px; đã reset cấu hình. **Không coi đây là kiểm thử production trên mobile.** Figma có màn 393 px, nhưng chưa chứng minh reflow hoặc accessibility của bản triển khai.

Video không có transcript khả dụng trong công cụ. Đã đọc mô tả và các chapter trên YouTube; không khẳng định đã xem/kiểm tra từng frame hay nghe toàn bộ lời thoại.

Kiểm tra deliverable: JSON đọc hợp lệ; CSV có 40 ID duy nhất; HTML kiểm tra cấu trúc bảng, mục lục và ảnh nhúng. Trình duyệt chặn mở tệp HTML cục bộ theo chính sách bảo mật, nên chưa xác minh bố cục HTML bằng preview. Ảnh production được kiểm tra trực tiếp trong quá trình audit.

#### Sổ bằng chứng

| ID | Nguồn, đường đi | Điều quan sát trực tiếp / mức độ |
|---|---|---|
| E01 | [Application](https://residents.ishdc.org/s/application), màn trước Start Application | Admissions: phí không hoàn lại; xử lý tối đa 2 business days; acceptance là temporary hold; bước 3 trong 5 ngày gồm agreement, ID, acceptance letter trường/internship, ảnh, emergency contact; có waitlist nếu không đủ chỗ |
| E02 | Application → Start Application | Personal Information, stepper 1–6 chỉ có số; tên, email, điện thoại, DOB, gender, địa chỉ, citizenship, dual citizenship, cultural heritage và nguồn giới thiệu; có Continue. Không đi tiếp bằng dữ liệu giả |
| E03 | Tab application đã mở sẵn tại Application Fee | Phí $50.00; Card Holder; Stripe card field; CTA Pay and Submit Application. Không tương tác với input thanh toán |
| E04 | [Portal Dashboard](https://residents.ishdc.org/s/) | Dropdown có hai Active Reservations; reservation [reservation mẫu] bắt đầu 01/11/2026, kết thúc 15/12/2026, Confirmed; Current deposit [số tiền mẫu]; Pay; feedback, emergency contact, bữa ăn, Wi-Fi. Không đưa mã truy cập vào deliverable |
| E05 | [Transaction Dashboard](https://residents.ishdc.org/s/transaction-dashboard) → Invoices History | Upcoming Payment, October balance, November charges đều $0; [invoice mẫu] [số tiền mẫu] và [invoice mẫu] [số tiền mẫu] đã Paid, remaining $0; Pay bị disable; có Download, chưa kiểm tra nội dung PDF |
| E06 | Transaction Dashboard → Payments History | Payment tháng 9 [số tiền mẫu] và tháng 10 [số tiền mẫu] tham chiếu reservation [reservation mẫu]; deposit [số tiền mẫu]; application fee $50 và application reference. Không phát lại giao dịch |
| E07 | Reservations admin (nguồn nội bộ) → [reservation mẫu] | List báo [tổng số bản ghi], [một trang kết quả]; các nguồn Application Form/Direct; Confirmed và Pending Approval; deposit riêng. [reservation mẫu]: Grand Total [số tiền mẫu] Deposit Not Paid, bed mẫu, 44 nights, ngày 01/11–15/12; có Rate Details, Reservation Invoices, Files, Activities, Check-In/Out |
| E08 | [reservation mẫu] → Rate Details / Reservation Invoices | Hai khoản [số tiền mẫu] cho 01/11 và [số tiền mẫu] cho 01/12, tổng [số tiền mẫu]; [invoice mẫu] và [invoice mẫu] đều Draft. Modal có chữ Approved trong khi các dòng là Draft; chưa xác định vai trò của chữ Approved |
| E09 | [reservation mẫu] → Reservation Invoices → [invoice mẫu] | Invoice Date 01/11/2026; Due Date 05/11/2026; dòng Date hiển thị 9/1/2026; Qty 30, Measure Night, Rate [số tiền mẫu] Total [số tiền mẫu]; Total/Balance [số tiền mẫu] Paid $0 |
| E10 | Rate Controller (nguồn nội bộ) | Rate Manager có Nightly Rate, X Nights Rate, Monthly Rate; chọn monthly hiện Start/End Month và năm; Room Type, Base Rate, refundability, Update Rates. Rate Grid có Type Monthly và Property/Room Type/Bed Type; bảng nhiều mức giá. Không áp dụng rate |
| E11 | Portal → Handbook | Link PDF chuyển tới trang có heading “Oops! That page can’t be found.” tại URL tài liệu handbook. Đây là lỗi truy cập nội dung xác minh trực tiếp, chưa kiểm tra mã HTTP |
| E12 | [Overnight Guests](https://residents.ishdc.org/s/overnight-guests) → New Request | Có một request NEW; form yêu cầu room, roommate, guest, ngày đến/đi; lựa chọn giới tính có Prefer not to answer; futon/linens, dietary, câu hỏi vaccination; thông báo ID/passport sau khi được duyệt; Send disabled khi trống. Chỉ mở/đóng |
| E13 | [Portal Reservations](https://residents.ishdc.org/s/reservations) | Hai dòng [reservation mẫu]/[reservation mẫu], room/date/status. Không thấy CTA tạo mới trong trạng thái và tài khoản đã kiểm tra; không suy ra mọi tài khoản đều không có |
| E14 | BN Invoices (nguồn nội bộ) → Filter → Search | Ban đầu 0 records; sau Search xuất hiện 25 dòng với Draft/Partial/Paid; footer vẫn ghi “25 of 0 records are displayed”. Dòng Paid vẫn có Days Due âm; chưa kiểm tra tất cả filter |
| E15 | Availability (nguồn nội bộ) → Show | Type Nightly, dates, Property/Room Type/Bed Type/Floor/Gender/Only Available; legend Reserved/Confirmed/Checked In/Checked Out/Out of Order/Unavailable. Show tải lịch; chưa thao tác ô, gán bed hoặc tạo reservation |
| E16 | Salesforce → Resident Applications | Có đối tượng Resident Applications, Recently Viewed báo 29 items; view chỉ có Resident Application Id, mã Waitlist-xxxx. Đây không phải tổng số application; tên kỹ thuật Waitlist không chứng minh tất cả hồ sơ đều đang waitlisted |
| E17 | [Important Information](https://residents.ishdc.org/s/important-information) | Nội dung dài gồm safety, house policies, community service, guests/local resources và policy; có nhiều link ngoài. Chỉ xác minh handbook hỏng, không gán trạng thái hỏng cho các link khác |
| F01 | [Figma page Student Portal](https://www.figma.com/design/6mmd7D0jfwSnDcWVwvNS2n/ISH?node-id=0-1) | Page Student Portal và Cover; Student Portal có 29 top-level frames trong 7 section; không thấy page admin/application trong inventory hiện tại |
| F02 | Figma Dashboard `1:1220`, Navigation `6:402` | Dashboard 1440 × 1995; nội dung news/map lớn; menu hamburger; My Rental và Pay Now; Start Nov 3, 2026 / End Apr 3, 2026; nhãn “Amount payabe”; Navigation có “Add New Reservation” nhưng chưa có frame đích tương ứng trong inventory |
| F03 | Figma Payments `1:2806`, Add Method `1:3694` | Overview, payment methods (bank/card), paid history, Receipt; Add Method form; chưa thấy invoice due/detail và checkout success/failure trong screen inventory; top-level reactions của mẫu này rỗng, chưa audit tất cả nested interactions |
| F04 | Figma Mobile Version, styles/variables API | 9 mobile frames, gồm Dashboard 393 × 2724, Payments 393 × 1415; local variable collections và local text styles trả về rỗng. Có instance Button/Icon Button, nên không suy ra không dùng component hoặc không có thư viện ngoài |
| F05 | Figma Student Portal cũ · OLD · node 2:47 | Ảnh New Reservation: Booking Term, thẻ loại phòng, ảnh/giá/tiện nghi, Select và Proceed; page NEW Design trống. Chỉ là tham chiếu lịch sử, chưa xác minh đang bật trên ISH. |
| V01 | [Video tham chiếu](https://www.youtube.com/watch?v=cbDme_9XLDs) | 7:16; mô tả kết nối reservations/rates/invoices/payments, placements, academic periods; nói semester/monthly/fixed-term, student reserve và approved transactions; đây là lời mô tả, chưa xác minh chức năng tương ứng trên ISH |

Bản chia sẻ công khai không chứa ảnh production, mã hồ sơ hay chi tiết giao dịch. Bằng chứng gốc được giữ trong bản nội bộ.

:::enddetails

:::details 3. Đối chiếu yêu cầu với hiện trạng

| Yêu cầu đã cung cấp | Production/Figma đã xác minh | Khoảng trống và điều kiện nghiệm thu |
|---|---|---|
| Modernize admin + portal + application | Admin có nghiệp vụ lớn; Figma chủ yếu portal | Cần bộ màn admin và application riêng; review theo task, không chỉ thẩm mỹ |
| Preserve functionality | Có admissions fee, hold, waitlist, hai reservation, invoice/payment, guests, documents/info | Tạo traceability từ chức năng cũ sang màn mới; chức năng chưa kiểm chứng không được tự xoá |
| Simplify workflows/navigation | Portal sidebar rõ mục; Figma chuyển sang hamburger và dashboard dài | Desktop dùng sidebar luôn hiện cho tác vụ thường xuyên; mobile điều hướng phù hợp; không làm mất discoverability |
| Standardized reusable package | Figma có component instances nhưng local tokens/styles chưa thấy | Core data contract + configurable policy + brand theme; ISH là profile cấu hình đầu tiên |
| ISH validation / future deployments | Chưa có UAT hoặc deployment trong audit này | Bộ kịch bản sandbox, đối soát số tiền, quyền và migration; khách thứ hai dùng cùng core với cấu hình khác |
| Video series Student Housing | Video hiện tại có cả admin và student | Kể một hồ sơ xuyên suốt, tách các tập theo kết quả; demo dữ liệu giả trong sandbox |

#### Đối chiếu video theo chapter

| Chapter công khai | Phạm vi kỳ vọng theo mô tả | Bằng chứng hiện tại / việc cần làm |
|---|---|---|
| 00:08–01:52 Reservations | Review và confirm placement | E07/E15 xác minh màn reservation, bed và availability; transition confirm chưa thử |
| 01:52–02:26 Payments/invoicing | Chuẩn bị giao dịch, quản lý payment | E05/E06/E08/E09/E14 có dữ liệu thực; quy tắc duyệt và phát hành cần sandbox |
| 02:26–03:56 Semester/monthly | Cấu hình theo kỳ | Monthly xác minh; chưa tìm thấy cấu hình Semester rõ ràng trên màn đã xem |
| 03:56–04:59 Fixed-term | Giá kỳ cố định | Có X Nights Rate nhưng chưa chứng minh tương đương fixed-term; cần mapping |
| 04:59–06:35 Portal | Reserve, housing details, transactions | E04/E05/E13; không thấy Reserve CTA trong trạng thái tài khoản mẫu |
| 06:35–07:16 Collect payments | Online payment | Có nút Pay và lịch sử Stripe; không thử charge/checkout |

Theo chapter, phần trước portal kéo dài 4:59; không dùng con số ~4,5 phút trong review cũ như mốc chính xác. Không coi demo 2025 là bản mô tả đầy đủ của production 2026.

:::enddetails

:::details 4. Findings và ưu tiên

P0: rủi ro chặn phát hành vì dữ liệu/tiền hoặc mất chức năng; P1: tác vụ cốt lõi; P2: hiệu quả và mở rộng. Ưu tiên dưới đây là đề xuất sản phẩm, không phải kết luận mọi mục đều là lỗi production.

| ID · mức | Bằng chứng / loại kết luận | Tác động | Hướng sửa và nghiệm thu |
|---|---|---|---|
| UX01 · P1 | E01/E16: application và reservation là các khái niệm tách biệt | Gộp hai luồng sẽ mất admission/hold/waitlist | Một journey có application ID và reservation ID liên kết; acceptance, giữ chỗ, confirmed có định nghĩa riêng; hiển thị deadline và checklist |
| UX02 · P1 | E02: stepper chỉ có số 1–6; bước đầu có nhiều nhóm dữ liệu | Người nộp khó ước lượng tiến độ và chuẩn bị | Tên bước, số bước, mục bắt buộc/tuỳ chọn, thời gian ước tính đã đo; review trước pay; save/resume chỉ đưa vào sau kiểm tra cơ chế |
| UX03 · P1 | E01/E03: fee nonrefundable và Pay and Submit gộp trong một CTA | Cần hiểu trả phí có đồng nghĩa được nhận/được phòng hay không | Summary luôn giải thích “phí xét đơn”, không bảo đảm admission/availability; tách trạng thái payment và submission, có receipt và recovery |
| UX04 · P1 | E04/E07/E06: deposit trên home [số tiền mẫu] trong khi [reservation mẫu] Not Paid; [số tiền mẫu] payment tham chiếu [reservation mẫu] | Deposit có thể ở cấp tài khoản/cũ/chuyển kỳ; người dùng dễ đọc sai | Hiển thị deposit amount, reservation áp dụng, collected/required/transfer pending; xác nhận quy tắc ledger trước đổi nhãn/số |
| UX05 · P1 | E05/E08/V01: portal $0, admin invoices Draft | Sinh viên có thể hiểu $0 là không còn chi phí | Phân biệt “phải trả”, “dự kiến chưa phát hành”, “đã trả”; nếu policy không cho lộ draft, chỉ hiển thị lịch dự kiến được phép, không đưa draft raw lên portal |
| UX06 · P0 gate | E09: header và line date lệch; Qty 30 Night nhưng Rate=Total=[số tiền mẫu] | Không giải thích được cơ sở tính, dễ đọc thành 30 × [số tiền mẫu] | Finance xác định date semantics và rate unit; render service period, basis, prorated amount; đối soát ledger. Không kết luận số tiền đang bị tính sai |
| UX07 · P1 | E04/E13: reservation tương lai nằm trong Active/Current; hai booking cùng tài khoản | Trộn current/upcoming và khó theo dõi đổi phòng | Thẻ Current stay/Upcoming/History dựa trên ngày và trạng thái; luôn hiện reservation context; kiểm tra ranh giới ngày chuyển phòng |
| UX08 · P1 | E13/V01/F02: có lời mô tả reserve và menu Figma nhưng chưa thấy luồng đích | Demo và self-service bị đứt đoạn | Thiết kế application entry, existing resident reserve/renew và admin-assisted entry; bật theo quyền/chính sách; room type preference khác bed assignment |
| UX09 · P1 | E05/E06/F03: Payments Figma nặng payment method/paid history | Chưa giải quyết chọn invoice, tiền còn lại, hạn, partial và failure | Invoice list/detail làm trung tâm; payment method là bước phụ; checkout/result/receipt có trạng thái pending/fail; không đánh đồng invoice với payment |
| UX10 · P1 | F01: không thấy admin/application screens trong file | Dễ phát hành portal đẹp nhưng workflow admin không đổi | Admin workspace cho application/reservation review, placement, rates, invoice review, payment reconciliation; liên kết record giữ context |
| UX11 · P1 | E11: Handbook mở trang không tìm thấy | Tài liệu thiết yếu không truy cập được | Cấu hình nguồn tài liệu có version/owner; kiểm tra link; fallback contact; sửa bằng quy trình thay đổi riêng sau audit |
| UX12 · P2 | E14: footer “25 of 0”; Paid vẫn có Days Due âm | Giảm tin cậy, dễ đọc Paid là quá hạn | Count theo query thật; empty/loading/error riêng; due label phụ thuộc balance/status; “Paid” không mang cảnh báo nợ |
| UX13 · P1 | E16: Recently Viewed chỉ có mã application | Phải mở từng bản ghi mới biết ai, lúc nào, trạng thái gì | Saved views theo công việc; applicant, requested dates, status, received date, hold deadline, missing items, owner; không sửa production view trong audit |
| UX14 · P2 | F02/F04: Dashboard desktop 1995 px, mobile 2724 px; news/map lớn | Chiếm chỗ của việc cần làm và thông tin lưu trú | Task queue đầu trang; amount due/hold/checklist/current stay; news/map sang Community/Help hoặc thu gọn; emergency/help vẫn dễ tìm |
| UX15 · P1 | F02: Start Nov 2026, End Apr 2026; stale notice; typo; tên/email/brand mẫu không nhất quán | Thiết kế giảm tin cậy và demo khó hiểu | Một fixture dataset duy nhất; end > start; số tiền thống nhất mọi màn; thông báo có thời hạn; sửa copy; initials theo tên |
| UX16 · P1 | F04: local variable collections/text styles rỗng | Khó đổi brand và giữ consistency | Semantic tokens, typography, components và state contracts; kiểm tra library ngoài trước xây lại; hai tenant demo bằng cùng component |
| UX17 · P2 | E02/E12: dữ liệu cá nhân/nhân khẩu học/health trong form | Cần mục đích và phạm vi thu thập rõ | Product/ISH xác nhận trường bắt buộc, giải thích mục đích và quyền xem; không tự thay policy. Nhãn AX guest dùng token nội bộ dù screenshot có nhãn đúng: kiểm tra accessible name/localization riêng |
| UX18 · P1 gate | Mobile production chưa kiểm tra thành công; keyboard/contrast chưa đo | Chưa có cơ sở tuyên bố accessible/responsive | Kiểm thử bàn phím, screen reader, 320/393/768/1440, zoom, lỗi form/checkout trong sandbox trước release |

#### Những điều cần giữ từ hệ thống hiện tại

Sidebar portal đã phân mục khá rõ; history phân invoice và payment; Paid vô hiệu hoá Pay; reservation có bed-level detail; deposit là trạng thái độc lập; invoice có Draft/Partial/Paid; availability/rate grid có filter theo cấu trúc property/room/bed. Revamp nên làm các mô hình đó dễ hiểu hơn. Không gom tất cả thành một số Amount payable hoặc một badge Confirmed.

:::enddetails

:::details 5. Workflow hiện tại và workflow đề xuất

#### 5.1 Admissions và bảo đảm chỗ

**Hiện tại đã xác minh một phần:** trang hướng dẫn → Start → Personal Information → [bước 2–5 chưa kiểm tra] → Application Fee $50 và Pay and Submit. Hướng dẫn nói tối đa 2 ngày làm việc → acceptance/temporary hold hoặc waitlist → trong 5 ngày hoàn thành agreement, ID, acceptance letter, photo, emergency contact. Hành vi gửi, email và việc chuyển application sang reservation chưa được tái hiện.

**Đề xuất:** Before you apply (eligibility, thời gian, fee, giấy tờ) → tên bước rõ → thông tin cá nhân → requested stay/preferences → hồ sơ cần thiết → review → payment + submit → tracking. Sau acceptance, hiển thị deadline có timezone của cơ sở, checklist và status từng tài liệu. Waitlist có requested dates, giải thích chưa giữ phòng, next update/contact. Chỉ hiển thị “Reservation secured” khi đủ điều kiện ISH đã duyệt.

Payment và submit cần hai kết quả độc lập: đã trả nhưng tạo đơn lỗi phải có reference và khôi phục, không yêu cầu trả lại ngay. Payment pending không được báo application đã hoàn tất khi backend chưa xác nhận.

#### 5.2 Reservation và placement

**Hiện tại:** portal liệt kê hai reservation Confirmed, dashboard chọn booking; admin list → record có room/bed/date/status, invoice và rate details; Availability có filters và lịch. Màn list có Pending Approval. Chưa xác minh thao tác confirm/gán bed.

**Đề xuất:** application/reservation queue → review completeness và preferences → availability theo term/date → chọn room type/bed có điều kiện → xem ảnh hưởng giá và xung đột → preview placement → confirm theo quyền → student thấy lịch lưu trú, room được công bố và next steps. Các thay đổi nhạy cảm cần activity trail.

Self-service Reserve a Room là cấu hình sản phẩm: có khách chỉ cho đăng ký preference, có khách cho chọn bed, có khách admin xếp phòng. ISH cần xác nhận chế độ; không hứa người nộp chắc chắn được tự chọn phòng.

#### 5.3 Rates và lịch thu

**Hiện tại:** Nightly/X Nights/Monthly; Rate Grid có property/room/bed. Reservation mẫu có [số tiền mẫu] + [số tiền mẫu] Video mô tả semester/monthly/fixed-term, nhưng academic period và semester chưa được xác minh trong màn ISH đã xem.

**Đề xuất:** chọn academic period/date range → rate plan (monthly/semester/fixed-term/nightly nếu khách dùng) → scope property/room/bed → rules (proration, inclusions, deposit, cancellation) → preview các booking đại diện → resolve overlap → approve/publish theo quyền. Rate đã dùng cần version để invoice cũ không tự đổi khi sửa giá mới.

Portal hiển thị “Giá theo tháng”, “Tổng cả kỳ” hoặc “Giá cố định cho khoảng ngày” đúng basis; lịch trả là khái niệm riêng. Ví dụ tổng fixed-term có thể trả nhiều đợt; không đổi tất cả thành `$ /month`.

#### 5.4 Invoices và payments

**Hiện tại:** reservation [reservation mẫu] có Draft invoices; reservation [reservation mẫu] có invoice đã trả và payment Stripe liên quan; portal có invoice/payment history. Approval visibility chỉ được hỗ trợ bởi mẫu dữ liệu và mô tả video, chưa thử transition.

**Đề xuất admin:** charge schedule → invoice Draft → review line/date/unit/tax/adjustment → approve/issue → student notification → payment attempts → allocations → reconciliation. Draft, issued, paid, overdue phải không dùng chung một flag. Overdue là điều kiện hạn + balance, không xoá trạng thái Partial.

**Đề xuất student:** Transactions → chọn invoice → service period + dòng tiền + đã trả/còn lại/hạn → review payment amount/method/fees → checkout → processing → success/failure/action required → receipt. Nếu người dùng đóng trang khi processing, history phải cho biết đang xử lý; retry không tạo charge trùng. Giảm paid balance chỉ khi đã nhận kết quả đáng tin cậy từ payment integration.

#### 5.5 Guest và dịch vụ cư dân

**Hiện tại:** New Request → form → Send; có row NEW và hướng dẫn upload ID sau approval. Important Information là nội dung dài; Handbook hỏng.

**Đề xuất:** guest request có thông tin phòng được phép và ngày phù hợp stay → review policy → submit → pending/approved/declined + reason → document checklist nếu cần. Maintenance, renewal, room change và termination là request riêng có policy, không cập nhật trực tiếp contract/bed từ portal. Figma termination nói minimum 14 days; **chưa coi đó là policy ISH production**.

:::enddetails

:::details 6. Kiến trúc trải nghiệm và mô hình dữ liệu mục tiêu

Portal desktop: **Home · Applications/Reservations · Transactions · Requests · Documents · Community/House info · Profile/Help**. Chỉ hiển thị nhóm mà role và tenant cho phép. Home thay đổi theo giai đoạn applicant/accepted/current/upcoming/alumni; không cần một dashboard đầy mọi card cho mọi người.

Admin: **Work queue · Applications · Reservations/Placement · Availability · Rates · Invoices · Payments/Reconciliation · Configuration**. Record workspace có header ID + status riêng + next action, timeline, tab hồ sơ, stay/bed, charges/invoices, payments, documents và activity. Giữ liên kết sâu về bản ghi Salesforce.

Mô hình sau là **logical model đề xuất**, không phải sơ đồ schema Salesforce đã kiểm chứng:

| Thực thể | Quan hệ và dữ liệu cần rõ |
|---|---|
| Student/Contact | Có nhiều application, reservation; identity không phải email free-text trong payment description |
| Application | Requested dates, preferences, admissions status, completeness, fee outcome, hold deadline, linked reservation(s) |
| AcademicPeriod | Tenant, tên kỳ, start/end, timezone, deadlines; chỉ bắt buộc khi model giá dùng kỳ |
| Reservation | Student, date range, reservation status, rate snapshot/version, total; không chứa duy nhất “deposit paid” cho toàn tài khoản |
| Placement/StaySegment | Reservation → property/room/bed, start/end; hỗ trợ chuyển phòng mà vẫn truy vết giá |
| RatePlan/RateVersion | Basis, scope, effective interval, proration, inclusions và approval; immutable snapshot khi dùng cho booking |
| Invoice/InvoiceLine | Reservation, service period, basis/quantity/unit price/amount, issue/due date, issued state, balance |
| Payment/Attempt/Allocation | Provider reference, result, amount, invoice allocation, deposit/application fee classification; một payment có thể phân bổ theo rule |
| DepositLedger | Collected/required/allocated/transferred/refunded và reservation context; quy tắc nghiệp vụ cần Finance chốt |
| Document/Request/Activity | Owner, record link, permission, status, version/deadline; timeline không lộ nội dung riêng cho người khác |

Không nên triển khai “one connected record” bằng cách gộp mọi object. Ý nghĩa sản phẩm là liên kết rõ và xem xuyên suốt, trong khi mỗi object giữ vòng đời riêng.

State model đề xuất: Application = Draft/Submitted/Under review/Waitlisted/Accepted/Declined/Withdrawn; Hold = Active/Expiring/Expired/Secured; Reservation = Pending/Confirmed/Cancelled và stay lifecycle riêng; Invoice = Draft/Issued/Void, settlement = Unpaid/Partial/Paid, overdue derived; Payment = Initiated/Processing/Action required/Succeeded/Failed/Refunded. Cần mapping từ enum thật trước khi migration; không tự đổi enum production theo bảng này.

:::enddetails

:::details 7. Reusable design system và configuration

#### Foundations

Hướng phù hợp với brief đã trích: admin dựa trên pattern SLDS, portal/public theo ngôn ngữ thương hiệu O:live/ISH cần xác nhận. Đây là định hướng thiết kế; chưa xác minh version SLDS hay nhận được bộ O:live gốc.

| Lớp | Quy tắc tái sử dụng |
|---|---|
| Primitive | Palette, spacing 4/8/12/16/24/32/48, radius, font scale và elevation; không rải màu cứng trong màn |
| Semantic | `text.primary`, `text.secondary`, `surface.canvas/card`, `border.default`, `action.primary`, `focus.ring`, `status.info/warning/success/danger` |
| Component | FormField, Stepper, Button/IconButton, Alert, StatusBadge, Money, DateRange, DataTable, FilterBar, EmptyState, Loading/Error, Modal/Drawer, TaskList |
| Domain | ReservationSummary/Selector, PlacementCard, RateBreakdown, InvoiceSummary/Lines, PaymentStatus/Receipt, DepositSummary, DocumentChecklist, HoldDeadline |
| Template | Public application wizard, student task dashboard, admin queue, record workspace, finance review, responsive list/detail |

Mỗi component cần default/hover/focus/disabled/loading/error và keyboard behavior; field có label/help/error, không chỉ placeholder. Badge luôn có chữ, không chỉ màu. Currency kèm unit/basis và thời kỳ. Không để UI nhận raw field name làm accessible label.

Đề xuất targets để kiểm chứng: body 16 px trong portal, tối thiểu 14 px cho dense table có zoom; vùng chạm thường dùng 44 px; contrast text thường 4.5:1, text lớn 3:1; focus luôn nhìn thấy, không bị sticky footer che. Đây là mục tiêu nghiệm thu thiết kế, chưa phải chứng nhận tuân thủ.

Mobile: form một cột, stepper “Bước 2/6 — …”, CTA không che nội dung; invoice table chuyển card/list có đủ amount/due/status; admin finance giữ table khi phù hợp với cuộn có nhãn; map tải theo nhu cầu; modal dài thành trang/scroll container có focus trap và trả focus khi đóng.

#### Core, tenant configuration và extension

| Core cố định | Cấu hình theo khách | Extension chỉ khi cần |
|---|---|---|
| IDs, relations, lifecycle contracts, permissions, Money/Date components, invoice/payment integrity, accessible patterns | Brand/logo, locale/currency/timezone, academic periods, application fields, fee/deposit policy, rate basis, room-selection mode, approval policy, document checklist, notices/links, modules | Học bổng tích hợp riêng, SSO đặc thù, custom contract provider hoặc custom accounting adapter |

File `student-housing-config.example.json` là **blueprint cấu hình**, không phải file chạy được trên production. Giá trị ISH có bằng chứng được gắn nguồn; các policy chưa xác minh để `null` và có `requiresConfirmation`. Không hard-code mức phí hiện tại thành mặc định cho mọi tenant. Không chứa password, access code hay payment secret.

Thứ tự xây library: audit library ngoài → tokens → form/navigation primitives → Money/Date/Status → domain components → page templates → fixtures và state coverage → hai theme. Điều kiện reusable: thêm khách mẫu thứ hai bằng cấu hình/theme, không copy riêng trang hay logic tính tiền.

:::enddetails

:::details 8. Screen inventory

#### Inventory Figma hiện tại — 29 frame, gồm 20 desktop và 9 mobile

| Section | Frames hiện có / node |
|---|---|
| Dashboard | Log in `1:1181`; Dashboard `1:1220`; Navigation `6:402`; Map `1:1541`; Map Dining selected `1:1893`; Add Guest `1:2278`; Request Room Change `38:4166`; Terminate Contract `39:4611` |
| Scholarships | Empty `1:3044`; List `1:3120`; Adding `1:3327` |
| Profile | Profile `1:3454` |
| Payments | Payments `1:2806`; Add New Payment Method `1:3694` |
| Documentation | Documentation `1:3980`; Important Information `1:4666` |
| Maintenance | List `23:3631`; Detail `23:3474`; New `14:1589`; Submitted `14:1828` |
| Mobile Version | Login `16:2216`; Navigation `16:3372`; Payments `16:2277`; Maintenance `42:5057`; Scholarships empty `16:2467`; form `34:3986`; Profile `16:2532`; Documentation `16:2750`; Dasboard `16:2844` |

Có 2 page: Student Portal và Cover trống. Việc không thấy màn trong inventory này không khẳng định màn không tồn tại trong file/branch khác hoặc trong sản phẩm.

#### Inventory mục tiêu

File `screen-inventory.csv` liệt kê các nhóm màn với priority và evidence. Đây là nhóm màn/luồng để estimate; mỗi nhóm còn có variants và state, không phải cam kết số artboard cuối cùng.

| Mã | Nhóm màn | Giai đoạn |
|---|---|---|
| A01–A09 | Before apply, wizard, review/fee, submission/result/recovery, status/hold/waitlist, checklist | Release 1 |
| S01–S07 | Login/recovery, task home, reservation list/detail, reserve/preferences, rate/schedule, documents | Release 1 |
| T01–T06 | Invoice list/detail, checkout review, processing/action-required, success/receipt, failure/retry, payment history | Release 1 |
| D01–D09 | Work queue, application review, reservation workspace, availability/placement, rates, rate preview, invoice queue/detail/approval, payment reconciliation | Release 1 |
| C01–C03 | Tenant config, roles/policy mapping, theme/component catalogue | Foundations + Release 1 |
| R01–R04 | Guest request/history, handbook/info/help, maintenance, change/renewal/termination | Preserve guests/info ở Release 1; phần còn lại Release 2 theo xác nhận |
| X01–X02 | Scholarships, Community/map | Release 2–3 nếu có nhu cầu thật |

Mọi luồng core có loading/empty/error/permission-denied và mobile treatment. Invoice phải có unpaid/partial/paid/overdue/draft visibility; reservation có no availability/waitlist/current/upcoming; payment có pending và failure; không chỉ thiết kế happy path.

:::enddetails

:::details 9. Roadmap và tiêu chí phát hành

Ước lượng dưới đây theo tuần làm việc sau khi có SME, sandbox và quyền đọc cấu hình; chưa phải lịch cam kết. Có thể chồng một phần thiết kế và implementation sau khi contract dữ liệu đã chốt.

| Giai đoạn | Khoảng thời gian đề xuất | Đầu ra / dependency | Gate |
|---|---|---|---|
| 0 — Xác thực nghiệp vụ | Tuần 1 | Traceability chức năng; walkthrough application 2–5 trong sandbox; mapping object/enum; quy tắc fee/deposit/proration/approval; kiểm tra UX06 | Product + Admissions + Finance chốt terms và bất thường dữ liệu |
| 1 — Foundations và prototype core | Tuần 2–3 | Tokens, components, tenant profile, fixtures; prototype applicant → admin placement → invoice → payment | Review end-to-end cả student/admin, gồm empty/error; không mất chức năng verified |
| 2 — Core package & ISH pilot | Tuần 4–7 | Application, portal, placement, rates, invoicing/payment và cấu hình; giữ guests/info; sửa handbook theo change được duyệt | Finance reconciliation, role tests, migration rehearsal, responsive/accessibility checks, UAT |
| 3 — Pilot và rollout | Tuần 8–9 | Pilot nhóm nhỏ, hỗ trợ vận hành, monitoring và rollback plan; cập nhật hướng dẫn | Không lệch balance/duplicate payment/mất hồ sơ; rollout theo quyết định owner |
| 4 — Tái sử dụng & nội dung | Tuần 10–11 | Tenant mẫu thứ hai; module đã xác nhận; quay series trong sandbox | Theme/config đổi được mà không fork core; mọi claim video có bằng chứng |

P0 trước phát hành: giải thích/đối soát date/unit/amount; không thu trùng khi retry; giữ history và reference; quyền portal theo chủ sở hữu; invoice draft không lộ ngoài policy; migration và rollback không làm mất liên kết. Đây là gates cần kiểm thử, không có kết luận rằng hệ thống hiện tại đang vi phạm tất cả.

#### Acceptance scenarios quan trọng

| Scenario sandbox | Kết quả cần kiểm chứng |
|---|---|
| Application trả phí thành công nhưng submit timeout | Một payment reference; resume hoặc hỗ trợ hoàn tất; không tự charge lần hai |
| Accepted nhưng chưa đủ document sau deadline | Trạng thái hold và next action đúng policy; không tự ghi confirmed sai |
| Không còn phòng trong requested dates | Waitlist rõ ràng; không hứa đã giữ bed |
| Cùng sinh viên có stay cũ và stay tương lai | Current/upcoming, invoice, deposit luôn gắn đúng reservation |
| Monthly nửa kỳ / leap year / đổi room | Finance ký xác nhận số tiền và service period; rate snapshot không thay booking cũ ngoài quy trình |
| Invoice Draft → Issued → Partial → Paid | Visibility, amount due, history và receipt đúng ở từng bước |
| Provider pending/failed/double click/webhook lặp | Không duplicate payment; status và recovery rõ; balance đối soát đúng |
| Paid invoice có due date đã qua | Hiển thị Paid, không nhãn nợ quá hạn sai |
| Resident A mở dữ liệu resident B | Bị từ chối; không lộ bản ghi/tài liệu |
| Keyboard + mobile + 200% zoom | Đi hết application/transaction tasks; focus/error/CTA vẫn dùng được |
| Migration | Counts, IDs, balances, documents, allocations khớp mẫu kiểm soát trước/sau |

#### Đo hiệu quả

Chưa có baseline analytics trong audit. Đo trước pilot rồi so sánh cùng cohort: completion và drop-off theo bước application; thời gian từ submitted đến reviewed; hold hoàn tất đúng hạn; thời gian xử lý placement; số bước/click tới invoice; payment completion và duplicate attempt; số ticket về số dư/đặt cọc; tỷ lệ link tài liệu hợp lệ; thời gian onboarding tenant mới và tỷ lệ component reuse.

Không dùng giảm thời gian/chi phí theo % trong marketing trước khi có phép đo. Đặt owner và event definition trước khi lập dashboard; không gửi PII, nội dung tài liệu hay card details vào analytics.

:::enddetails

:::details 10. Quyết định chưa đủ bằng chứng

| Câu hỏi cần owner xác nhận | Owner đề xuất | Điều bị ảnh hưởng |
|---|---|---|
| Application tạo reservation lúc nào? Acceptance/hold/secure có state thật nào? | Admissions + Salesforce | Journey, mapping và migration |
| ISH cho chọn room/bed hay chỉ preference? Existing resident reserve/renew ở đâu? | Housing Operations | Reserve UI và quyền |
| [số tiền mẫu] deposit ở tài khoản mẫu là carried balance hay thuộc stay cũ? Transfer thế nào? | Finance | Deposit summary và allocations |
| Invoice line date và Rate/Qty/Measure biểu thị gì? Vì sao khác header? | Finance + Engineering | UX06 và gate tài chính |
| Draft visibility và Approved là invoice status, filter hay hành động gì? | Finance + Salesforce | Invoice workflow |
| Semester/fixed-term/academic period hiện map vào object/module nào? | Product + Salesforce | Standard package |
| Proration, tax, refund/cancellation và partial payment được phép ra sao? | Finance | Price/checkout contract |
| O:live library/source và SLDS target đã chốt ở đâu? | Design Lead | Tokens và component reuse |
| Maintenance, scholarships, room change, renewal, termination đang chạy ở hệ thống nào? | Product + ISH | Scope release 2 và preserve list |
| Yêu cầu 14 ngày notice trong Figma và các trường health/demographic còn đúng policy nào? | ISH policy owner | Copy/validation; không tự sửa nghiệp vụ |

Không cần chờ tất cả câu trả lời để sửa copy fixture, thiết kế queue, lập tokens hay prototype invoice. Các phần tính tiền, state transition và migration phụ thuộc các quyết định tương ứng.

:::enddetails

:::details 11. Storyboard cho Student Housing niche series

**Trục kể chuyện:** một hồ sơ sinh viên đi từ application đến chỗ ở và khoản thanh toán có thể truy vết. Mỗi tập có vấn đề → thao tác → kết quả → next step. Dùng cùng fixture “Alex Morgan”, kỳ Fall Demo 2027, tenant Demo House; tên/room/money/receipt đều giả. Màn chưa triển khai phải có nhãn “Proposed experience” hoặc “Prototype”. Không quay/đưa ảnh production hoặc credential/mã phòng vào video.

#### Tập 1 — “Từ application tới sẵn sàng nhập ở” · 75 giây

| Thời gian | Hình / thao tác | Voice-over gợi ý | Bằng chứng cần có trước quay |
|---|---|---|---|
| 0–8s | Applicant thấy Before you apply, fee và 3 mốc | “Biết cần chuẩn bị gì trước khi bắt đầu.” | Fee/policy demo được cấu hình rõ |
| 8–23s | Wizard có tên bước, preferences, review | “Điền một lần, xem lại trước khi gửi.” | Không hứa save/resume nếu chưa làm |
| 23–35s | Sandbox fee/result, application reference | “Phí xét đơn và kết quả xét duyệt là hai trạng thái riêng.” | Payment mock/sandbox; result xác nhận |
| 35–51s | Admin queue → application detail | “Admissions thấy hồ sơ thiếu gì và bước tiếp theo.” | Workflow sandbox, quyền đúng |
| 51–67s | Accepted + hold deadline + checklist | “Sinh viên theo dõi các việc cần hoàn tất để giữ chỗ.” | Deadline/checklist thực hoạt động |
| 67–75s | Kết quả Ready + CTA xem demo | “Một hành trình rõ ràng cho cả sinh viên và đội vận hành.” | Nếu prototype, nhãn luôn nhìn thấy |

#### Tập 2 — “Placement rõ ràng, theo từng bed” · 60 giây

| Thời gian | Hình / thao tác | Voice-over gợi ý | Bằng chứng cần có |
|---|---|---|---|
| 0–7s | Một request có preferred dates/type | “Preference chưa phải là phòng đã xác nhận.” | Data fixture thống nhất |
| 7–24s | Admin workspace → availability có filters | “Đối chiếu ngày ở và chỗ còn trống ngay trong cùng ngữ cảnh.” | Availability sandbox có dữ liệu |
| 24–40s | Chọn placement → preview rate/conflict | “Xem tác động trước khi xác nhận.” | Conflict/rate preview đã implement hoặc nhãn prototype |
| 40–53s | Confirm trong sandbox, portal Upcoming | “Sinh viên thấy lịch và trạng thái của reservation.” | Transition chứng minh được |
| 53–60s | ID liên kết về record, CTA | “Theo dõi placement xuyên suốt vòng đời lưu trú.” | Không khẳng định thuật toán tự xếp phòng |

#### Tập 3 — “Monthly, semester hay fixed-term?” · 70 giây

| Thời gian | Hình / thao tác | Voice-over gợi ý | Bằng chứng cần có |
|---|---|---|---|
| 0–9s | Ba rate basis cạnh nhau | “Mỗi mô hình nhà ở có cách báo giá khác nhau.” | Các basis thực sự được hỗ trợ |
| 9–28s | Chọn period, scope và rate plan | “Cấu hình theo kỳ và loại phòng.” | Semester/academic mapping đã được xác nhận |
| 28–45s | Preview full term và nửa kỳ | “Xem trước tổng phí và lịch thu theo quy tắc của cơ sở.” | Finance xác nhận proration |
| 45–61s | Portal hiện basis + schedule | “Sinh viên thấy tổng kỳ và khoản đến hạn riêng biệt.” | UI/số liệu đồng nhất |
| 61–70s | Theme thứ hai cùng component | “Một nền tảng, cấu hình cho từng mô hình.” | Chưa có tenant demo thì ghi concept |

#### Tập 4 — “Từ invoice được duyệt đến receipt” · 75 giây

| Thời gian | Hình / thao tác | Voice-over gợi ý | Bằng chứng cần có |
|---|---|---|---|
| 0–8s | Admin Draft có service period/line items | “Kiểm tra chi tiết trước khi phát hành.” | Finance UI đã được duyệt |
| 8–24s | Review → issue trong sandbox | “Chỉ khoản đã được phát hành mới trở thành việc cần trả.” | Visibility policy thật |
| 24–42s | Portal Due → invoice detail → review payment | “Biết trả cho kỳ nào, đã trả bao nhiêu và còn lại bao nhiêu.” | Amount và allocation đúng |
| 42–56s | Processing → sandbox success | “Theo dõi kết quả, kể cả khi giao dịch cần thêm thời gian.” | Không quay charge production |
| 56–68s | Receipt → payment/invoice/reservation links | “Receipt và lịch sử luôn gắn với khoản thu liên quan.” | Provider reference/receipt demo |
| 68–75s | Một failure state ngắn + CTA | “Có hướng xử lý rõ ràng nếu thanh toán chưa hoàn tất.” | Failure/retry đã kiểm chứng |

#### Tập 5 — “Tự phục vụ trong thời gian lưu trú” · 55 giây

| Thời gian | Hình / thao tác | Voice-over gợi ý | Bằng chứng cần có |
|---|---|---|---|
| 0–10s | Task home trên mobile | “Việc cần làm ở ngay đầu trang.” | Mobile thật đã kiểm thử |
| 10–27s | Guest request → pending → document next step | “Gửi yêu cầu và biết điều gì diễn ra tiếp theo.” | Guest workflow sandbox |
| 27–43s | Handbook, house info, contact dễ tìm | “Tìm thông tin thiết yếu khi cần.” | Link/version hợp lệ |
| 43–55s | Maintenance detail/status, CTA | “Theo dõi yêu cầu trong cùng portal.” | Chỉ dùng khi module có thật; nếu chưa có, thay bằng guest history |

#### Tập 6 — “ISH và gói Student Housing có thể tái sử dụng” · 60 giây

| Thời gian | Hình / thao tác | Voice-over gợi ý | Bằng chứng cần có |
|---|---|---|---|
| 0–10s | Core journey thu nhỏ | “Từ hồ sơ đến placement và payment, các bước được liên kết.” | End-to-end demo |
| 10–27s | Đổi brand/locale/period trong tenant demo | “Mỗi cơ sở cấu hình thương hiệu và chính sách riêng.” | Không sửa production; config thực |
| 27–43s | Hai portal, cùng domain components | “Tái sử dụng trải nghiệm đã được kiểm chứng.” | Reuse được chứng minh, không chỉ hai ảnh |
| 43–53s | Pilot metrics có nguồn hoặc nhãn chưa đo | “ISH là use case đầu tiên để xác thực gói mới.” | Chỉ nêu chỉ số đã đo |
| 53–60s | CTA “Khám phá Student Housing” | “Xem workflow phù hợp với mô hình của bạn.” | Landing/demo URL được đội marketing chốt |

Từ mỗi tập cắt 15–25 giây cho social theo một hành động và một kết quả. Video overview 2–3 phút ghép tập 1/2/4; video walkthrough dài dành cho buyer kỹ thuật giữ cả admin và portal. Giữ chữ lớn, cursor có mục đích, zoom vào record ID/service period/status; không quay toàn màn hình dày chữ rồi tua nhanh.

Claim ledger: “có history, linked invoice/payment, bed detail, fee application” có bằng chứng production; “semester/fixed-term/approved visibility” mới có mô tả hoặc xác minh một phần; “giảm X%, zero errors, tự động xếp phòng, triển khai khách mới trong X ngày” chưa có bằng chứng và không dùng.

:::enddetails

:::details 12. Handoff

Ưu tiên làm ngay trên thiết kế: sửa fixture dates/copy, bổ sung invoice/checkout states, tạo application/hold/checklist, thiết kế admin work queue/placement và định nghĩa tokens. Trước implementation tài chính, Finance cần chốt UX06 và deposit context. Trước rollout, chạy các acceptance scenario trong sandbox và đối soát migration.

Bộ deliverable gồm báo cáo này, bản HTML dễ đọc, screen inventory CSV, cấu hình blueprint JSON và ảnh bằng chứng đã chọn. Không có thay đổi production hoặc Figma được thực hiện trong audit.

:::enddetails

:::details Phụ lục ảnh bằng chứng

Ảnh bằng chứng chỉ có trong bản audit nội bộ.

#### E02 — Personal Information

Ảnh được giữ trong bản audit nội bộ, không đăng công khai.

#### E03 — Application Fee, chưa nhập thẻ hoặc gửi đơn

Ảnh được giữ trong bản audit nội bộ, không đăng công khai.

#### E05 — Portal Invoice History

Ảnh được giữ trong bản audit nội bộ, không đăng công khai.

#### E08 — Hai invoice Draft trong admin

Ảnh được giữ trong bản audit nội bộ, không đăng công khai.

#### E09 — Header dates và line item cần đối soát

Ảnh được giữ trong bản audit nội bộ, không đăng công khai.

Ảnh được giữ trong bản audit nội bộ, không đăng công khai.

#### E11 — Handbook mở trang không tìm thấy

Ảnh được giữ trong bản audit nội bộ, không đăng công khai.

:::enddetails
