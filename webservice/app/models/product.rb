class Product < ActiveRecord::Base
  validates :name,
    presence: true,
    length: { minimum: 2, maximum: 40 }

  validates :company,
    presence: true

  validates :origin,
    presence: true

  validates :description,
    presence: true

  validates :rate,
    presence: true
end
