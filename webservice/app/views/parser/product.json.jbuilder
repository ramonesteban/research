if !@product.nil?
  json.extract! @product, :name, :company, :origin, :description, :rate
else
  json.status 'error'
  json.message 'not a valid product'
end
