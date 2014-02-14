json.array!(@products) do |product|
  json.extract! product, :id, :name, :company, :origin, :description, :rate
  json.url product_url(product, format: :json)
end
