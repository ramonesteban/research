class ParserController < ApplicationController
  def product
    product = params[:id]
    @product = Product.find_by(id: product)
    json_string = render_to_string(formats: :json)
    json_object = JSON.parse(json_string)
    render json: JSON.pretty_generate(json_object)
  end

  def products
    @products = Product.all
    json_string = render_to_string(formats: :json)
    json_object = JSON.parse(json_string)
    render json: JSON.pretty_generate(json_object)
  end

  def script
    value = %x(python --version 2>&1)
    path = Rails.root.join('public').to_s
    response = %x(python #{path}/ocr.py)
    render text: response
  end
end
