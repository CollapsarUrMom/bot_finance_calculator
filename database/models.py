from sqlalchemy import DateTime, Float, String, func
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())


class Product(Base):
    __tablename__ = 'product'

    # id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), primary_key= True, nullable=False)
    price: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    quantity:Mapped[int] = mapped_column()
    suma:Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False)
    time:Mapped[int] = mapped_column()