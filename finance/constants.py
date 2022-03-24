CLIENT_TYPE_INDIVIDUAL = 1
CLIENT_TYPE_COMPANY = 2

CLIENT_TYPES = [
    (CLIENT_TYPE_INDIVIDUAL, 'Individual'),
    (CLIENT_TYPE_COMPANY, 'Company')
]

PROJECT_TYPE_BUDGET = 1
PROJECT_TYPE_HOURLY_FT = 2
PROJECT_TYPE_HOURLY_PT = 3
PROJECT_TYPE_CONTRACT = 4

PROJECT_TYPES = [
    (PROJECT_TYPE_BUDGET, 'Budget'),
    (PROJECT_TYPE_HOURLY_FT, 'Hourly FT'),
    (PROJECT_TYPE_HOURLY_PT, 'Hourly PT'),
    (PROJECT_TYPE_CONTRACT, 'Contract'),
]

PROJECT_STATUS_ONGOING = 1
PROJECT_STATUS_PAUSED = 2
PROJECT_STATUS_ENDED = 3

PROJECT_STATUS = [
    (PROJECT_STATUS_ONGOING, 'Ongoing'),
    (PROJECT_STATUS_PAUSED, 'Paused'),
    (PROJECT_STATUS_ENDED, 'Ended'),
]

WEEKLY = 1
BI_WEEKLY = 2
MONTHLY = 3

PAYMENT_PERIOD = [
    (WEEKLY, 'Weekly'),
    (BI_WEEKLY, 'Bi-Weekly'),
    (MONTHLY, 'Monthly')
]

FINANCIAL_TYPE_SND_INVOICE = 1
FINANCIAL_TYPE_SND_PAYMENT = 2
FINANCIAL_TYPE_RCV_PAYMENT = 3
FINANCIAL_TYPE_REFUND_PAYMENT = 4

FINANCIAL_TYPES = [
    (FINANCIAL_TYPE_SND_INVOICE, 'Send Invoice'),
    (FINANCIAL_TYPE_SND_PAYMENT, 'Send Payment'),
    (FINANCIAL_TYPE_RCV_PAYMENT, 'Receive Payment'),
    (FINANCIAL_TYPE_REFUND_PAYMENT, 'Refund payment')
]

FINANCIAL_TYPES_DICT = {
    FINANCIAL_TYPE_SND_INVOICE: "Send Invoice",
    FINANCIAL_TYPE_SND_PAYMENT: "Send Payment",
    FINANCIAL_TYPE_RCV_PAYMENT: "Receive Payment",
    FINANCIAL_TYPE_REFUND_PAYMENT: "Refund Payment"
}

FINANCIAL_STATUS_PENDING = 1
FINANCIAL_STATUS_APPROVED = 2
FINANCIAL_STATUS_DECLINED = 3
FINANCIAL_STATUS_CANCELED = 4

FINANCIAL_STATUS = [
    (FINANCIAL_STATUS_PENDING, 'Pending'),
    (FINANCIAL_STATUS_APPROVED, 'Approved'),
    (FINANCIAL_STATUS_DECLINED, 'Declined'),
    (FINANCIAL_STATUS_CANCELED, 'Canceled')
]

PAYMENT_PLATFORM_PAYPAL = 'paypal'
PAYMENT_PLATFORM_PAYONEER = 'payoneer'
PAYMENT_PLATFORM_UPWORK = 'upwork'
PAYMENT_PLATFORM_FREELANCER = 'freelancer'
PAYMENT_PLATFORM_TOPTAL = 'toptal'
PAYMENT_PLATFORM_BINANCE = 'binance'
PAYMENT_PLATFORM_METAMASK = 'metamask'
PAYMENT_PLATFORM_BANK = 'bank'
PAYMENT_PLATFORM_USDT = 'usdt'
PAYMENT_PLATFORM_USDC = 'usdc'


PAYMENT_PLATFORMS = [
    (PAYMENT_PLATFORM_PAYPAL, 'PayPal'),
    (PAYMENT_PLATFORM_PAYONEER, 'Payoneer'),
    (PAYMENT_PLATFORM_UPWORK, 'Upwork'),
    (PAYMENT_PLATFORM_FREELANCER, 'Freelancer'),
    (PAYMENT_PLATFORM_TOPTAL, 'Toptal'),
    (PAYMENT_PLATFORM_BINANCE, 'Binance'),
    (PAYMENT_PLATFORM_METAMASK, 'MetaMask'),
    (PAYMENT_PLATFORM_BANK, 'Bank'),
    (PAYMENT_PLATFORM_USDT, 'USDT'),
    (PAYMENT_PLATFORM_USDC, 'USDC'),
]
